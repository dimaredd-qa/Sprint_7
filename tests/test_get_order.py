import allure
import requests
from data import Endpoint

class TestGetOrder:
    @allure.title('Проверка получения списка заказов')
    @allure.description(f'на ручке {Endpoint.get_order_url}')
    def test_get_order(self):
        response = requests.get(f'{Endpoint.get_order_url}')
        assert response.status_code == 200 and 'orders' in response.json()