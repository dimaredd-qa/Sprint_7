import pytest
import requests
import generator
from data import Endpoint


def data_for_courier():
    return {
        "login": generator.login_generator(),
        "password": generator.password_generator(),
        "firstName": generator.name_generator(),
        "lastName": generator.last_name_generator(),
        "address": generator.address_generator(),
        "metroStation": generator.metro_station_generator(),
        "phone": generator.phone_generator(),
        "rentTime": generator.rent_time_generator(),
        "deliveryDate": generator.delivery_date_generator(),
        "comment": generator.comment_generator()
    }

@pytest.fixture
def for_reg_delete_cour():
    data = data_for_courier()
    reg_new_cour = {"login": data["login"], "password": data["password"], "firstName": data["firstName"]}
    yield reg_new_cour
    auth_data = {"login": data["login"], "password": data["password"]}
    try:
        auth_resp = requests.post(Endpoint.login_courier_url, json=auth_data)
        if auth_resp.status_code == 200:
            requests.delete(f"{Endpoint.create_courier_url}/{auth_resp.json()['id']}")
    except requests.exceptions.RequestException:
        pass

@pytest.fixture
def for_auth_delete_cour():
    data = data_for_courier()
    requests.post(f'{Endpoint.create_courier_url}', json=data)
    auth_data = {"login": data["login"], "password": data["password"]}
    login_no_passwd = {"login": data["login"], "password": ""}
    passwd_no_login = {"login": "", "password": data["password"]}
    yield [data, auth_data, login_no_passwd, passwd_no_login]
    try:
        auth_resp = requests.post(Endpoint.login_courier_url, json=auth_data)
        if auth_resp.status_code == 200:
            requests.delete(f"{Endpoint.create_courier_url}/{auth_resp.json()['id']}")
    except requests.exceptions.RequestException:
        pass

@pytest.fixture
def create_delete_order():
    data = data_for_courier()
    response = requests.post(Endpoint.create_order_url, json=data)
    track = response.json()["track"]

    yield response
    requests.put(Endpoint.delete_order_url, params={"track": track})

@pytest.fixture
def get_courier_and_order_ids(for_auth_delete_cour):
    data = data_for_courier()
    courier_resp = requests.post(Endpoint.login_courier_url, json=for_auth_delete_cour[1])
    courier_id = courier_resp.json()["id"]
    order_resp = requests.post(Endpoint.create_order_url, json=data)
    order_id = order_resp.json()["track"]
    yield courier_id, order_id
    requests.put(Endpoint.delete_order_url, params={"track": order_id})