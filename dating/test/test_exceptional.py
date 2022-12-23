from rest_framework.test import APITestCase
from dating.models import *
from dating.test.TestUtils import TestUtils

class DatingAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(user_id=101,name="user1",age=25,email="user1@gmail.com",
        phone= 9841849651,gender= "Male",city="Vikarabad",country= "India")
        InterestsModel.objects.create(id=1,interested_in="Walking",not_interested_in="Running",
        hobbies="GYM",profile_url="myprofile2.com",about= "I am married",user_id= 102)
        MatchModel.objects.create(id=2,match_id=112,user_id= 102)
        LikesModel.objects.create(id=1,like_id=1112,user_id= 101)
        DisLikesModel.objects.create(id=1,dislike_id=2222,user_id= 101)
 
    def test_get_the_user_by_id_error(self):
        url='http://127.0.0.1:8000/user_crud_pk/1011/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetTheUserByIdError", True, "exception")
            print("TestGetTheUserByIdError = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheUserByIdError", False, "exception")
            print("TestGetTheUserByIdError = Failed")


    def test_update_user_error(self):
        url='http://127.0.0.1:8000/user_crud_pk/1012/'
        data={
                'gender':'Female'
            }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestUpdateUserError", True, "exception")
            print("TestUpdateUserError = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateUserError", False, "exception")
            print("TestUpdateUserError = Failed")

    def test_delete_user_error(self):
        url='http://127.0.0.1:8000/user_crud_pk/1011/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteUserError", True, "exception")
            print("TestDeleteUserError = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteUserError", False, "exception")
            print("TestDeleteUserError = Failed")


#Interests Module 

    def test_get_the_interests_by_id_error(self):
        url='http://127.0.0.1:8000/interests_crud_pk/11/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetTheInterestsByIdError", True, "exception")
            print("TestGetTheInterestsByIdError = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheInterestsByIdError", False, "exception")
            print("TestGetTheInterestsByIdError = Failed")

    def test_get_the_interests_by_user_id_error(self):
        url='http://127.0.0.1:8000/get_interests_by_user_id/102222/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetTheInterestsByUserIdError", True, "exception")
            print("TestGetTheInterestsByUserIdError = Passed")
        else:
            test_obj.yakshaAssert("TestGetTheInterestsByUserIdError", False, "exception")
            print("TestGetTheInterestsByUserIdError = Failed")

    def test_update_interests_error(self):
        url='http://127.0.0.1:8000/interests_crud_pk/11/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("TestUpdateInterestsError", True, "exception")
            print("TestUpdateInterestsError = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateInterestsError", False, "exception")
            print("TestUpdateInterestsError = Failed")

    def test_delete_interests_error(self):
        url='http://127.0.0.1:8000/interests_crud_pk/11/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteInterestsError", True, "exception")
            print("TestDeleteInterestsError= Passed")
        else:
            test_obj.yakshaAssert("TestDeleteInterestsError", False, "exception")
            print("TestDeleteInterestsError = Failed")


#Likes Module

    def test_get_all_likes_by_user_id_error(self):
        url='http://127.0.0.1:8000/get_likes_by_user_id/1011/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetAllLikesByUserIdError", True, "exception")
            print("TestGetAllLikesByUserIdError = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllLikesByUserIdError", False, "exception")
            print("TestGetAllLikesByUserIdError = Failed")

#DisLikes Module

    def test_add_dislike_error(self):
        url='http://127.0.0.1:8000/add_dislike/'
        data=  {
        "dislike_id": 2223,
        "user_id": 101
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestAddDislikeError", True, "exception")
            print("TestAddDislikeError = Passed")
        else:
            test_obj.yakshaAssert("TestAddLikeError", False, "exception")
            print("TestAddDislikeError = Failed")

    def test_get_all_dislikes_by_user_id_error(self):
        url='http://127.0.0.1:8000/get_dislikes_by_user_id/1011/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetAllDislikeByUserIdError", True, "exception")
            print("TestGetAllDislikeByUserIdError = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDislikeByUserIdError", False, "exception")
            print("TestGetAllDislikeByUserIdError = Failed")