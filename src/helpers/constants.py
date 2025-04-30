import pytest


class URLS:
    BASE_URL = 'https://ez-route.stand.praktikum-services.ru/'


class Addresses:
    ADDRESS_1 = 'Хамовнический вал, 34'
    ADDRESS_2 = 'Зубовский бульвар, 37'


class TorAndInterfaces:
    ROUTE_RESULT_ONE_ADDRESS = 'Авто Бесплатно В пути 0 мин.'
    MOVEMENT_OPTIONS = {'car', 'walk', 'taxi', 'bike', 'scooter', 'drive'}
    ROUTE_MODES = {'Оптимальный', 'Быстрый', 'Свой'}
    TARIFF_OPTIONS = {'Рабочий', 'Сонный', 'Отпускной', 'Разговорчивый', 'Утешительный', 'Глянцевый'}
    TAXI_FIELDS_TO_FILL = {'Телефон', 'Способ оплаты', 'Комментарий водителю', 'Требования к заказу'}
    TAXI_TARIFF_DESCRIPTION = {'Рабочий': 'Для деловых особ, которых отвлекают',
                               'Сонный': 'Для тех, кто не выспался',
                               'Отпускной': 'Если пришла пора отдохнуть',
                               'Разговорчивый': 'Если мысли не выходят из головы',
                               'Утешительный': 'Если хочется свернуться калачиком',
                               'Глянцевый': 'Если нужно блистать'
                               }
    CAR_WAITING_HEADER = 'Поиск машины'
    ORDER_SETTING_BUTTONS = {'Отменить', 'Детали'}
    COMPLETION_HEADER = 'мин. и приедет'
    DRIVER_INFO = {'Имя', 'Фото', 'Рейтинг'}


class TestParameters:
    ONE_ADDRESS = [Addresses.ADDRESS_1, Addresses.ADDRESS_2]
    TWO_ADDRESSES = [
        (Addresses.ADDRESS_1, Addresses.ADDRESS_2),
        (Addresses.ADDRESS_2, Addresses.ADDRESS_1)
    ]
    SWITCH_BETWEEN_TARIFFS = [('Оптимальный', 'Быстрый'),
                              ('Быстрый', 'Оптимальный')
                              ]
    TAXI_TARIFF = ['Рабочий', pytest.param('Сонный', marks=pytest.mark.xfail(reason="Баг: неправильное значение")),
                   'Отпускной',
                   pytest.param('Разговорчивый', marks=pytest.mark.xfail(reason="Баг: неправильное значение")),
                   'Утешительный', 'Глянцевый']
