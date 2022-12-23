from rest_framework.test import APITestCase
from dating.models import *
from dating.test.TestUtils import TestUtils
class DatingAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(user_id=101,name="user1",age=25,email="user1@gmail.com",
        phone= 9841849651,gender= "Male",city="Vikarabad",country= "India")
        InterestsModel.objects.create(id=1,interested_in="Walking",not_interested_in="Running",
        hobbies="GYM",profile_url="myprofile2.com",about= "I am married",user_id= 102)
        MatchModel.objects.create(id=2,match_id=112,user_id= 102)
        LikesModel.objects.create(id=1,like_id=1112,user_id= 101)
        DisLikesModel.objects.create(id=1,dislike_id=2222,user_id= 101)
 
    def test_get_the_user_by_id(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetTheUserById", True, "functional")
            print("TestGetTheUserById = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheUserById", False, "functional")
            print("TestGetTheUserById = Failed")

    def test_get_all_users(self):
        url='http://127.0.0.1:8000/user_crud/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllUsers", True, "functional")
            print("TestGetAllUsers = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllUsers", False, "functional")
            print("TestGetAllUsers = Failed")

    def test_register_user(self):
        url='http://127.0.0.1:8000/user_crud/'
        data= {
        "user_id": 102,
        "name": "User2",
        "age": 31,
        "email": "user2@gmail.com",
        "phone": 9841849651,
        "gender": "Male",
        "city": "Vikarabad,",
        "country": "India"
    }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestRegisterUser", True, "functional")
            print("TestRegisterUser = Passed")
        else:
            test_obj.yakshaAssert("TestRegisterUser", False, "functional")
            print("TestRegisterUser = Failed")

    def test_update_user(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        data={
                'gender':'Female'
            }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestUpdateUser", True, "functional")
            print("TestUpdateUser = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateUser", False, "functional")
            print("TestUpdateUser = Failed")

    def test_delete_user(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteUser", True, "functional")
            print("TestDeleteUser = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteUser", False, "functional")
            print("TestDeleteUser = Failed")


#Interests Module 
    def test_create_interests(self):
        url='http://127.0.0.1:8000/interests_crud/'
        data=  {
        "id":3,    
        "interested_in": "Walking",
        "not_interested_in": "Running",
        "hobbies": "GYM",
        "profile_url": "myprofile2.com",
        "about": "I am married",
        "user_id": 102  
    }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestCreateInterests", True, "functional")
            print("TestCreateInterests = Passed")
        else:
            test_obj.yakshaAssert("TestCreateInterests", False, "functional")
            print("TestCreateInterests = Failed")

    def test_get_the_interests_by_id(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetTheInterestsById", True, "functional")
            print("TestGetTheInterestsById = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheInterestsById", False, "functional")
            print("TestGetTheInterestsById = Failed")

    def test_get_the_interests_by_user_id(self):
        url='http://127.0.0.1:8000/get_interests_by_user_id/102/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetTheInterestsByUserId", True, "functional")
            print("TestGetTheInterestsByUserId = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheInterestsByUserId", False, "functional")
            print("TestGetTheInterestsByUserId = Failed")

    def test_update_interests(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        data= {
        "id":1,
        "interested_in": "Walking",
        "not_interested_in": "Running",
        "hobbies": "GYM",
        "profile_url": "myprofile2.com",
        "about": "I am un married",
        "user_id": 102  
         }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestUpdateInterests", True, "functional")
            print("TestUpdateInterests = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateInterests", False, "functional")
            print("TestUpdateInterests = Failed")

    def test_delete_interests(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteInterests", True, "functional")
            print("TestDeleteInterests= Passed")
        else:
            test_obj.yakshaAssert("TestDeleteInterests", False, "functional")
            print("TestDeleteInterests = Failed")


#Match Module 
    def test_create_match(self):
        url='http://127.0.0.1:8000/match_view/'
        data=  {
        "match_id": 112,
        "user_id": 102
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestCreateMatch", True, "functional")
            print("TestCreateMatch = Passed")
        else:
            test_obj.yakshaAssert("TestCreateMatch", False, "functional")
            print("TestCreateMatch = Failed")


    def test_get_all_matches(self):
        url='http://127.0.0.1:8000/match_view/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllMatches", True, "functional")
            print("TestGetAllMatches = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllMatches", False, "functional")
            print("TestGetAllMatches = Failed")


#Likes Module

    def test_add_like(self):
        url='http://127.0.0.1:8000/add_like/'
        data=  {
        "like_id": 1112,
        "user_id": 101
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestAddLike", True, "functional")
            print("TestAddLike = Passed")
        else:
            test_obj.yakshaAssert("TestAddLike", False, "functional")
            print("TestAddLike = Failed")

    def test_get_all_likes_by_user_id(self):
        url='http://127.0.0.1:8000/get_likes_by_user_id/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllLikesByUserId", True, "functional")
            print("TestGetAllLikesByUserId = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllLikesByUserId", False, "functional")
            print("TestGetAllLikesByUserId = Failed")

#DisLikes Module

    def test_add_dislike(self):
        url='http://127.0.0.1:8000/add_dislike/'
        data=  {
        "dislike_id": 2223,
        "user_id": 101
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestAddDislike", True, "functional")
            print("TestAddDislike = Passed")
        else:
            test_obj.yakshaAssert("TestAddLike", False, "functional")
            print("TestAddDislike = Failed")

    def test_get_all_dislikes_by_user_id(self):
        url='http://127.0.0.1:8000/get_dislikes_by_user_id/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllDislikeByUserId", True, "functional")
            print("TestGetAllDislikeByUserId = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDislikeByUserId", False, "functional")
            print("TestGetAllDislikeByUserId = Failed")