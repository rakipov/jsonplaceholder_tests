import allure
from hamcrest import assert_that, equal_to
from framework.helper import broken_data
from framework.check import check_add_new_post_response, check_add_incorrect_post
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestAddPosts:

    @allure.title('Positive. Add new post')
    def test_add_post(self, some_data):
        response = Client().add_new_post(some_data)
        check_add_new_post_response(response)
        assert_that(response.json()['title'], equal_to(some_data['title']))
        assert_that(response.json()['body'], equal_to(some_data['body']))
        assert_that(response.headers['Content-Type'], equal_to('application/json; charset=utf-8'))

    @allure.title('Negative. Incorrect body')
    def test_add_incorrect_post(self):
        response = Client().add_new_post(data=broken_data())
        check_add_incorrect_post(response)
