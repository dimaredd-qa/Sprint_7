import generator


class Endpoint:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    create_courier_url = f'{main_url}api/v1/courier'
    login_courier_url = f'{main_url}api/v1/courier/login'
    create_order_url = f'{main_url}api/v1/orders'
    delete_order_url = f'{main_url}api/v1/orders/cancel'
    get_order_url = f'{main_url}/api/v1/orders'
    get_order_by_track_url = f'{main_url}/api/v1/orders/track'
    accept_order_url = f"{main_url}/api/v1/orders/accept"

class DataForRegistration:
    reg_data = [
        {'password': generator.password_generator(), 'firstName': generator.name_generator()},
        {'login': generator.login_generator(), 'firstName': generator.name_generator()}
    ]

class DataCreateOrder:
    order = {
    "firstName": generator.name_generator(),
    "lastName": generator.last_name_generator(),
    "address": generator.address_generator(),
    "metroStation": generator.metro_station_generator(),
    "phone": generator.phone_generator(),
    "rentTime": generator.rent_time_generator(),
    "deliveryDate": generator.delivery_date_generator(),
    "comment": generator.comment_generator()
}
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

