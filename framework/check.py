import allure
from framework.helper import get_expected_response_data
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_by_id_response(response):
    _response_general_check(response)


@allure.step
def check_get_user_info_by_id_response(response):
    _response_general_check(response)
    assert_that(response.json(), equal_to(get_expected_response_data()))


@allure.step
def check_get_user_info_by_null_id_response(response):
    assert_that(len(response.json()), equal_to(0))


@allure.step
def check_add_new_post_response(response, expected_code):
    assert_that(response.status_code, equal_to(expected_code))


@allure.step
def check_get_post_by_null_id(response, expected_code):
    assert_that(response.status_code, equal_to(expected_code))


@allure.step
def check_add_incorrect_post(response, expected_code):
    assert_that(response.status_code, equal_to(expected_code))
