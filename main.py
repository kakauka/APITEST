from telethon import TelegramClient
import pytest
import requests
import allure
import asyncio
import pytest_asyncio
import utils


@allure.feature('Создание детей с валидными данными')
def test_Children_сreate_valid(): #Создание ребенка с валидными данными
    """
    Создание ребенка с валидными данными
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': 'Test',
                                   'birth_date':'2022-03-24',
                                   'sex': 'male',
                                   "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_name(): #Создание ребенка с невалидными данными, пустое имя
    """
    Создание ребенка с невалидными данными, пустое имя
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': '   ',
                                   'birth_date': '2022-03-24',
                                   'sex': 'male',
                                   "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['This field may not be blank.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
                print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_notvalid_nameT2(): #Создание ребенка с невалидными данными, некорректное имя со спец симв
    """
    Создание ребенка с невалидными данными, некорректное имя со спец симв
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': ' %5Bac9^&* )',
                                   'birth_date': '2022-03-24',
                                   'sex': 'male',
                                   "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['Invalid name']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
                print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_birth_date():#Создание ребенка с невалидными данными, пустая дата рождения
    """
    Создание ребенка с невалидными данными, пустая дата рождения
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': 'Test',
                                   'birth_date': '',
                                   'sex': 'male',
                                   "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'birth_date': ['Date has wrong format. Use one of these formats instead: YYYY-MM-DD.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
                print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_birth_dateT2(): #Создание ребенка с невалидными данными, некорректная дата рождения
    """
    Создание ребенка с невалидными данными, некорректная дата рождения
    """
    response = requests.post(utils.urlChildrenList,
                                 headers=utils.header,
                                 json={'name': 'Test',
                                       'birth_date': '0111-10-11',
                                       'sex': 'male',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "birth_date": [
            "The year of birth can't be less than 1900"
        ]
    }
}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
                print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_sex(): #Создание ребенка с невалидными данными, пустой пол
    """
    Создание ребенка с невалидными данными, пустой пол
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': 'Test',
                                   'birth_date': '2022-04-05',
                                   'sex': '',
                                   "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'sex': ['"" is not a valid choice.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_sexT2(): #Создание ребенка с невалидными данными, неизвестный пол
    """
    Создание ребенка с невалидными данными, неизвестный пол
    """
    response = requests.post(utils.urlChildrenList,
                                 headers=utils.header,
                                 json={'name': 'Test',
                                       'birth_date': '2022-04-05',
                                       'sex': 'xaxa',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'sex': ['"xaxa" is not a valid choice.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature('Создание детей с невалидными данными')
def test_children_create_novalid_empty(): #Создание ребенка с невалидными данными, пустые поля
    """
    Создание ребенка с невалидными данными, пустые поля
    """
    response = requests.post(utils.urlChildrenList,
                             headers=utils.header,
                             json={'name': '',
                                   'birth_date': '',
                                   'sex': '',
                                   "kinship": ""})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "name": [
            "This field may not be blank."
        ],
        "birth_date": [
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
        ],
        "sex": [
            "\"\" is not a valid choice."
        ],
        "kinship": [
            "\"\" is not a valid choice."
        ]
    }
}
    with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Получение списка детей")
def test_ChildrenList(): #Получение списка с количеством детей
    """
        Получение списка с количеством детей
    """
    response = requests.get(utils.urlChildrenList, headers=utils.header)
    response.body = response.json()['count']
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        with allure.step(f"Общее количество детей \n {response.json()['count']}"):
            print(str(response.json()['count']))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_name():  # update ребенка с невалидными данными, некорректное имя
    """
        update ребенка с невалидными данными, некорректное имя
    """
    response = requests.put(utils.urlChildrenUpdate,
                                 headers=utils.header,
                                 json={'name': ' T%!@&% 1S)S ',
                                       'birth_date': '2022-02-11',
                                       'sex': 'male',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['Invalid name']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_nameT2():  # update ребенка с невалидными данными, некорректное имя(пустое)
    """
        update ребенка с невалидными данными, некорректное имя(пустое)
    """
    response = requests.put(utils.urlChildrenUpdate,
                                    headers=utils.header,
                                    json={'name': '    ',
                                          'birth_date': '2022-02-11',
                                          'sex': 'male',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['This field may not be blank.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_bith_date():  # update ребенка с невалидными данными, некоррекная дата рождения
    """
        update ребенка с невалидными данными, некоррекная дата рождения
    """
    response = requests.put(utils.urlChildrenUpdate,
                            headers=utils.header,
                            json={'name': 'UpdateTest',
                                  'birth_date': '0111-10-11',
                                  'sex': 'male',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {"status_code": 400,"errors": {"birth_date": ["The year of birth can't be less than 1900"]}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_bith_dateT2():  # update ребенка с невалидными данными, некоррекный mail (пустой)
    """
        update ребенка с невалидными данными, некоррекный mail (пустой)
    """
    response = requests.put(utils.urlChildrenUpdate,
                            headers=utils.header,
                            json={'name': 'UpdateTest',
                                  'birth_date': '',
                                  'sex': 'male',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'birth_date': ['Date has wrong format. Use one of these formats instead: YYYY-MM-DD.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_sex():  # update ребенка с невалидными данными, неизвестный пол
    """
        update ребенка с невалидными данными, неизвестный пол
    """
    response = requests.put(utils.urlChildrenUpdate,
                            headers=utils.header,
                            json={'name': 'UpdateTest',
                                  'birth_date': '',
                                  'sex': 'xaxa',
                                       "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'birth_date': ['Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'], 'sex': ['"xaxa" is not a valid choice.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_sexT2():  # update ребенка с невалидными данными, пустой пол и дата рождения
    """
        update ребенка с невалидными данными, пустой пол и дата рождения
    """
    response = requests.put(utils.urlChildrenUpdate,
                            headers=utils.header,
                            json={'name': 'UpdateTest',
                                  'birth_date': '',
                                  'sex': '',
                                  "kinship": "father"})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'birth_date': ['Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'], 'sex': ['"" is not a valid choice.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Update детей с невалиднымы данными")
def test_children_update_novalid_empty():  # update ребенка с невалидными данными, все поля пустые
    """
        update ребенка с невалидными данными, все поля пустые
    """
    response = requests.put(utils.urlChildrenUpdate,
                            headers=utils.header,
                            json={'name': '',
                                  'birth_date': '',
                                  'sex': '',
                                  "kinship": ""})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "name": [
            "This field may not be blank."
        ],
        "birth_date": [
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
        ],
        "sex": [
            "\"\" is not a valid choice."
        ],
        "kinship": [
            "\"\" is not a valid choice."
        ]
    }
}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))


@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_name():  #  изменение профиля с невалидными данными, некорректное имя
    """
       изменение профиля с невалидными данными, некорректное имя
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': ' $@%!*@% ',
                                  'email': 'test@mail.com',
                                  'phone': '+79151112233',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['Invalid name']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_nameT2():  # изменение профиля с невалидными данными, некорректное имя(пустое)
    """
       изменение профиля с невалидными данными, некорректное имя(пустое)
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': '',
                                  'email': 'test@gmail.com',
                                  'phone': '+79150361122',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'name': ['This field may not be blank.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_email():  # изменение профиля с невалидными данными, некорректный email
    """
       изменение профиля с невалидными данными, некорректный email
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': ' tS2#$%^&*est@gm@*)ail.com',
                                  'phone': '+79150361122',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "email": [
            "Invalid email"
        ]
    }
}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_phone():  # изменение профиля с невалидными данными, некорректный телефон
    """
      изменение профиля с невалидными данными, некорректный телефон
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test001@mail.com',
                                  'phone': '79150361122',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'phone': ['The phone number entered is not valid.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))


@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_phoneT2():  # изменение профиля с невалидными данными, некорректный телефона
    """
      изменение профиля с невалидными данными, некорректный телефона
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test001@mail.com',
                                  'phone': '9150361122',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'phone': ['The phone number entered is not valid.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_phoneT3():  # изменение профиля с невалидными данными, некорректный номер телефона
    """
     изменение профиля с невалидными данными, некорректный номер телефона
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test001@mail.com',
                                  'phone': '791503611225',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'phone': ['The phone number entered is not valid.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))





@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_notifications():  # изменение профиля с невалидными данными, некорректный notifications и номер телефона
    """
     изменение профиля с невалидными данными, некорректный notifications и номер телефона
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test@mail.com',
                                  'phone': '791503611225',
                                  'notifications_enabled': 'tr',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {'status_code': 400, 'errors': {'phone': ['The phone number entered is not valid.'], 'notifications_enabled': ['Must be a valid boolean.']}}
        with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_notificationsT2():  # изменение профиля с невалидными данными, некорректный notifications (пустой)
    """
     изменение профиля с невалидными данными, некорректный notifications (пустой)
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test@mail.com',
                                  'phone': '+79150361127',
                                  'notifications_enabled': '',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "notifications_enabled": [
            "Must be a valid boolean."
        ]
    }
}
    with allure.step(f"Посмотрим что получили \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_language():  # изменение профиля с невалидными данными, некорректный язык
    """
     изменение профиля с невалидными данными, некорректный язык
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test@mail.com',
                                  'phone': '+79150361127',
                                  'notifications_enabled': 'true',
                                  'language': 'CN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "language": [
            "\"CN\" is not a valid choice."
        ]
    }
}
    with allure.step(f"Посмотрим что получили \n {response.json()}"):
        print(str(response.json()))

@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_languageT2():  # изменение профиля с невалидными данными, некорректный язык (пустой)
    """
     изменение профиля с невалидными данными, некорректный язык (пустой)
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test@mail.com',
                                  'phone': '+79150361127',
                                  'notifications_enabled': 'true',
                                  'language': ''})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
    "status_code": 400,
    "errors": {
        "language": [
            "\"\" is not a valid choice."
        ]
    }
}
    with allure.step(f"Посмотрим что получили \n {response.json()}"):
        print(str(response.json()))


@allure.feature("Изменение профиля с невалидными данными")
def test_profile_change_novalid_phone_and_mail():  # изменение профиля с невалидными данными, пустой телефон и email
    """
    Изменение профиля с невалидными данными, пустой  телефон и email
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': '',
                                  'phone': '',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json() == {
	"status_code": 400,
	"errors": {
		"non_field_errors": [
			"Phone or email required"
		]
	}
}

@allure.feature("Изменение профиля с валидными данными")
def test_profile_change_valid_phone():  # изменение профиля с валидными данными, изменяем на пустой номер телефона
    """
     изменение профиля с валидными данными, изменяем на пустой номер телефона
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test001@mail.com',
                                  'phone': '',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json()['phone'] == None
        with allure.step(f"Получили пустое значение =  \n {response.json()['phone']}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с валидными данными")
def test_profile_change_valid_email():  # изменение профиля с валидными данными, изменяем на пустой email
    """
     изменение профиля с валидными данными, изменяем на пустой email
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': '',
                                  'phone': '+79150361127',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json()['email'] == None
        with allure.step(f"Получили пустое значение =  \n {response.json()['email']}"):
            print(str(response.json()))

@allure.feature("Изменение профиля с валидными данными")
def test_profile_change_valid_all():  # изменение профиля с валидными данными, все поля
    """
     изменение профиля с валидными данными, все поля
    """
    response = requests.patch(utils.urlProfileCreate,
                            headers=utils.header,
                            json={'name': 'Сергей',
                                  'email': 'test@mail.com',
                                  'phone': '+79150361127',
                                  'notifications_enabled': 'true',
                                  'language': 'EN'})
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        assert response.json()['name' or 'email'] == 'Сергей','test@mail.com'
        with allure.step(f"Получили значение =  \n {response.json()}"):
            print(str(response.json()))

@allure.feature("Получение списка c MainGoals")
def test_maingoals_list(): #Получение списка c MainGoals
    """
        Получение списка c MainGoals
    """
    response = requests.get(utils.urlMainGoalList, headers=utils.header)
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        with allure.step(f"Возможно есть данные:  \n {response.json()['results']}"):
            print(str(response.json()))

@allure.feature("Получение списка c Missions")
def test_maissions_list(): #Получение списка c Missions
    """
        Получение списка c Missions
    """
    response = requests.get(utils.urlMissionsList, headers=utils.header)
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        with allure.step(f"Возможно есть данные:  \n {response.json()['results']}"):
            print(str(response.json()))


@allure.feature("Получение списка c Character-clothes")
def test_character_clothes_list(): #Получение списка c Character-clothes
    """
        Получение списка c character-Clothes
    """
    response = requests.get(utils.urlCharacterclothesList, headers=utils.header)
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        with allure.step(f"Возможно есть данные:  \n {response.json()['results']}"):
            print(str(response.json()))


@allure.feature("Генерация телеграм кода")
def test_get_generation_code(): #Генерация телеграмм кода
    """
         Получение сгенерированного кода
    """
    response = requests.patch(utils.urlTelegramGenerete, headers=utils.header)
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step("Запрос отправлен"):
        responsecode = response.json()['code']
        return responsecode

@allure.feature("Генерация телеграм кода")
def test_generation_code():#Генерация телеграмм кода
    """
         Проверка кода и передача для телеграм бота
    """
    code = test_get_generation_code()
    assert code
    return '/start ' + code

@allure.feature("Отправка невалидного кода телеграм боту")
@pytest.mark.parametrize("user", ["@FirstGadgetTestBot",]) #Отправка невалидного кода телеграм боту
def test_send_message_novalid_code(user):
    """
         Отправка невалидного кода телеграм боту
    """
    message = "/start 111111"
    with allure.step(f"Код отправлен, {message}"):
        with utils.client:
            utils.client.loop.run_until_complete(utils.mains(user,message))

@allure.feature("Отправка валидного кода телеграм боту")
@pytest.mark.parametrize("user", ["@FirstGadgetTestBot",]) #Отправка валидного кода телеграм боту
def test_send_message_valid_code(user):
    """
         Отправка валидного кода телеграм боту
    """
    message = test_generation_code()
    with allure.step(f"Код отправлен, {message}"):
        with utils.client:
            utils.client.loop.run_until_complete(utils.mains(user,message))



@allure.feature("Проверка подтверждения телеграмм профиля")
def test_check_succes_profile_telegram(): #Проверка подтверждения телеграмм профиля
    """
         Проверка подтверждения телеграмм профиля
    """
    response = requests.get(utils.urlTelegramMe, headers=utils.header)
    with allure.step(f'Status code {response.status_code}'):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Запрос отправлен, профиль подтвержден:  \n {response.json()}"):
        assert response.json() == {
	"id": 5586326845,
	"username": "FirstGadget"
}
        print(str(response.json()))

