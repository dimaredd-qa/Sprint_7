import pytest
import allure
import requests
from data import Endpoint

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description(f'на ручке {Endpoint.login_courier_url}')
    def test_login_courier_true(self, for_auth_delete_cour):
        response = requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[1])
        assert response.status_code == 200 and "id" in response.json()

    @allure.title('Проверка авторизации без логина')
    @allure.description(f'на ручке {Endpoint.login_courier_url}')
    def test_login_courier_no_login(self, for_auth_delete_cour):
        response = requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[3])
        assert response.status_code == 400 and response.json() == {"message":  "Недостаточно данных для входа"}

    @allure.title('Проверка авторизации без пароля')
    @allure.description(f'на ручке {Endpoint.login_courier_url}')
    def test_login_courier_no_password(self, for_auth_delete_cour):
        response = requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[2])
        assert response.status_code == 400 and response.json() == {"message":  "Недостаточно данных для входа"}

    @allure.title('Проверка авторизации незарегистрированного курьера')
    @allure.description(f'на ручке {Endpoint.login_courier_url}')
    def test_login_courier_no_reg(self, for_reg_delete_cour):
        response = requests.post(f'{Endpoint.login_courier_url}', json=for_reg_delete_cour)
        assert response.status_code == 404 and response.json() == {"message": "Учетная запись не найдена"}