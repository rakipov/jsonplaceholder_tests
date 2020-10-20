import allure
import pytest
from framework.check import check_get_all_posts_response, check_get_post_by_id_response, check_get_post_by_null_id
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check_get_all_posts_response(response)

    @allure.title('Positive. Get post by id')
    @pytest.mark.parametrize('post_id', [1, 10, 4])
    def test_get_post_by_id(self, post_id):
        response = Client().get_post_by_id(post_id=post_id)
        check_get_post_by_id_response(response)

    @allure.title('Negative. Get post by null id')
    def test_get_post_by_null_id(self):
        response = Client().get_post_by_id(post_id=-2)
        check_get_post_by_null_id(response)
