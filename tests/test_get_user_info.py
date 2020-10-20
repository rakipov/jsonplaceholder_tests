import allure
import pytest
from framework.check import check_get_user_info_by_id_response, check_get_user_info_by_null_id_response
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts')
class TestGetPosts:

    @pytest.mark.parametrize('user_id', [10])
    @pytest.mark.parametrize('name', ['Clementina DuBuque'])
    @pytest.mark.parametrize('email', ['Rey.Padberg@karina.biz'])
    @allure.title('Positive. Get user info by id')
    def test_get_user_info_by_id(self, user_id, name, email):
        response = Client().get_user_info_by_id(user_id=user_id)
        check_get_user_info_by_id_response(response, name, email)

    @allure.title('Negative. Get user info by null id')
    def test_get_user_info_by_null_id(self):
        response = Client().get_user_info_by_id(user_id=11)
        check_get_user_info_by_null_id_response(response)
