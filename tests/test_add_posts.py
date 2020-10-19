import allure
import pytest
from mimesis import Text
from framework.check import check_add_new_post_response
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestAddPosts:

    @pytest.fixture
    def some_data(self):
        text = Text('en')
        data = {
            'title': text.text(quantity=2),
            'body': text.text(quantity=2),
            'userId': 1
        }
        return data

    @allure.title('Positive. Add new post')
    def test_add_post(self, some_data):
        response = Client().add_new_post(some_data)
        check_add_new_post_response(response)
        assert response.json()['title'] == some_data['title']
        assert response.json()['body'] == some_data['body']
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    @allure.title('Negative. Incorrect body')
    def test_incorrect_body(self):
        body = Text('en')
        response = Client().add_new_post(data={
            'title': 'test_title',
            'body': body.text(quantity=1400),
            'userId': 1
        })
        assert response.status_code == 500
