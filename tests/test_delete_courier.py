import allure
import requests
from data import Endpoint

class TestDeleteCourier:
    @allure.title('Проверка удаления курьера')
    @allure.description(f'на ручке {Endpoint.create_courier_url}/:id')
    def test_delete_courier(self, for_auth_delete_cour):
        response_user = requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[1])
        delete = requests.delete(f'{Endpoint.create_courier_url}/{response_user.json()["id"]}')
        assert delete.status_code == 200 and delete.json() == {"ok": True}

    @allure.title('Проверка удаления курьера без id')
    @allure.description(f'на ручке {Endpoint.create_courier_url}/:id')
    def test_delete_courier_no_id(self, for_auth_delete_cour):
        requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[1])
        delete = requests.delete(f'{Endpoint.create_courier_url}')
        assert delete.status_code == 400 and delete.json() == {"message":  "Недостаточно данных для удаления курьера"}

    @allure.title('Проверка удаления курьера с несуществующим id(буквы)')
    @allure.description(f'на ручке {Endpoint.create_courier_url}/:id')
    def test_delete_courier_no_existing_id(self):
        delete = requests.delete(f'{Endpoint.create_courier_url}/курьер')
        assert delete.status_code == 404 and delete.json() == { "message": "Курьера с таким id нет"}

    @allure.title('Проверка удаления курьера с уже удаленным id')
    @allure.description(f'на ручке {Endpoint.create_courier_url}/:id')
    def test_delete_already_deleted_courier(self, for_auth_delete_cour):
        with allure.step('Получаем id курьера'):
            response_user = requests.post(f'{Endpoint.login_courier_url}', json=for_auth_delete_cour[1])
            courier_id = response_user.json()['id']
            assert response_user.status_code == 200, "Авторизация не удалась"
            assert 'id' in response_user.json(), "В ответе отсутствует id курьера"
        with allure.step('Удаляем курьера (первый раз — успешно)'):
            delete_response = requests.delete(f'{Endpoint.create_courier_url}/{courier_id}')
            assert delete_response.status_code == 200 and delete_response.json() == {"ok": True}
        with allure.step('Пытаемся удалить его снова (должен вернуть 404)'):
            delete_again_response = requests.delete(f'{Endpoint.create_courier_url}/{courier_id}')
            assert delete_again_response.status_code == 404 and delete_again_response.json() == {"message": "Курьера с таким id нет"}