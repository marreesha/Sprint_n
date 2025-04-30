import pytest
import allure
from src import TestParameters, TorAndInterfaces


@allure.feature('Подготовка к заказу такси')
class TestTaxiOrderPreparation:

    @allure.story('Переключение между видами маршрута')
    @allure.title('Проверка переключения между "{first_mode}" и "{second_mode}" маршрутами')
    @pytest.mark.parametrize('first_mode, second_mode', TestParameters.SWITCH_BETWEEN_TARIFFS)
    def test_shift_between_fast_optimal(self, route_types, first_mode, second_mode):
        route_types.click_on_mode(first_mode)
        first_mode_text = route_types.get_route_result()
        active_mode = route_types.get_active_mode()
        assert active_mode == first_mode

        route_types.click_on_mode(second_mode)
        second_mode_text = route_types.get_route_result()
        active_mode = route_types.get_active_mode()
        assert active_mode == second_mode

        with allure.step('Данные теста'):
            allure.attach(str(first_mode_text), name='first_mode_text')
            allure.attach(str(second_mode_text), name='second_mode_text')

        assert first_mode_text != second_mode_text

    @allure.story('Переключение между видами маршрута')
    @allure.title('Проверка переключения на вид маршрута "Свой"')
    def test_shift_to_custom_mode(self, route_types):
        route_types.click_on_mode('Свой')
        active_mode = route_types.get_active_mode()
        assert active_mode == 'Свой'

        displayed_transport = route_types.get_displayed_transport()

        with allure.step('Данные теста'):
            allure.attach(str(active_mode), name='active_mode')
            allure.attach(str(displayed_transport), name='displayed_transport')

        assert displayed_transport == TorAndInterfaces.MOVEMENT_OPTIONS

    @allure.story('Активность кнопок заказа')
    @allure.title('Проверка активности кнопки "Вызвать такси" для маршрута "Быстрый"')
    def test_taxi_button_is_active_fast_mode(self, route_types):
        route_types.click_on_mode()

        assert route_types.taxi_button_is_active() is True

    @allure.story('Активность кнопок заказа')
    @allure.title('Проверка активности кнопки "Забронировать" для типа передвижения "Драйв"')
    def test_book_button_is_active_drive_mode(self, route_types):
        route_types.click_on_mode('Свой')
        route_types.click_on_drive()

        assert route_types.book_button_is_active() is True
