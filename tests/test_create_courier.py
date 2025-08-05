import pytest
import allure
import requests
from data import Endpoint, DataForRegistration

class TestCreateCourier:
    @allure.title('Проверка создания нового курьер')
    @allure.description(f'на ручке {Endpoint.create_courier_url}')
    def test_create_courier(self, for_reg_delete_cour):
        response = requests.post(f'{Endpoint.create_courier_url}', json=for_reg_delete_cour)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Проверка создания существующего курьер')
    @allure.description(f'на ручке {Endpoint.create_courier_url}')
    def test_create_existing_courier_failed(self, for_auth_delete_cour):
        again_create = requests.post(f'{Endpoint.create_courier_url}', json=for_auth_delete_cour[0])
        assert again_create.status_code == 409 and again_create.json() == {"message": "Этот логин уже используется"}

    @allure.title('Проверка создания курьер без одного обязательного поля')
    @allure.description(f'на ручке {Endpoint.create_courier_url}')
    @pytest.mark.parametrize('data', DataForRegistration.reg_data)
    def test_create_courier_deficit_data_failed(self, data):
        response = requests.post(f'{Endpoint.create_courier_url}', json=data)
        assert response.status_code == 400 and response.json() == {"message": "Недостаточно данных для создания учетной записи"}