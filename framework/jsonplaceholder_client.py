import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, data: dict):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=data)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_user_info_by_id(self, user_id: int):
        return self._get(path=f'/users/{user_id}')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def add_new_post(self, data):
        return self._post(path=f'/posts/', data=data)
