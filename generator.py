from faker import Faker


fake_ru = Faker('ru_RU')

def login_generator():
    generated_login = fake_ru.user_name()
    return generated_login

def password_generator():
    generated_password = fake_ru.random_number(8)
    return generated_password

def name_generator():
    generated_name = fake_ru.first_name()
    return generated_name

def last_name_generator():
    generated_lastname = fake_ru.last_name()
    return generated_lastname

def address_generator():
    generated_address = fake_ru.address()
    return generated_address

def metro_station_generator():
    generated_metro_station = fake_ru.random_int(min=1, max=20)
    return generated_metro_station

def phone_generator():
    generated_phone = fake_ru.phone_number()
    return generated_phone

def rent_time_generator():
    generated_rent_time = fake_ru.random_int(min=1, max=5)
    return generated_rent_time

def delivery_date_generator():
    generated_delivery_date = fake_ru.future_date(end_date='+30d').strftime('%Y-%m-%d')
    return generated_delivery_date

def comment_generator():
    generated_comment = fake_ru.sentence()
    return generated_comment
