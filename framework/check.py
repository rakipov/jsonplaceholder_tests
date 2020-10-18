import allure
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. '
                f'Actual code: {response.status_code}. '
                f'Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_by_id_response(response):
    _response_general_check(response)


@allure.step
def check_add_new_post_response(response, expected_code=201):
    assert_that(response.status_code, equal_to(expected_code))
