import pytest
import allure
import requests
from data import Endpoint, DataCreateOrder

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description(f'на ручке {Endpoint.create_order_url}')
    @pytest.mark.parametrize('scooter_color', DataCreateOrder.scooter_color)
    def test_create_order(self, scooter_color, create_delete_order):
        order_data = DataCreateOrder.order
        order_data['color'] = scooter_color
        order = requests.post(f'{Endpoint.create_order_url}', json=order_data)
        assert order.status_code == 201 and "track" in order.json()