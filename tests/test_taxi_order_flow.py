import pytest
import allure
from selenium.common import TimeoutException
from src import TorAndInterfaces, TestParameters


@allure.feature('Заказ такси')
class TestTaxiOrderFlow:

    # Не очень понятно, что тут хотели авторы курса, поэтому ыло произведено разделение на несколько тестов
    @allure.story('Полный флоу заказа такси с проверкой окна ожидания')
    def test_taxi_order_flow_waiting_screen(self, taxi_order):
        taxi_order.click_on_tariff('Рабочий')
        taxi_order.choose_laptop_table()

        taxi_order.confirm_order()  # совершаем заказ

        title, timer_visibility = taxi_order.get_waiting_status()
        # Проверка элементов окна ожидания машины
        assert title == TorAndInterfaces.CAR_WAITING_HEADER
        assert timer_visibility is True

        cancel_btn, details_btn = taxi_order.get_order_setting_btn_status()
        # Проверка кнопок настройки заказа
        assert cancel_btn is True
        assert details_btn is True

    @allure.story('Полный флоу заказа такси с проверка окна завершенного заказа')
    def test_taxi_order_flow_completion_screen(self, taxi_order):
        taxi_order.click_on_tariff('Рабочий')
        taxi_order.choose_laptop_table()
        taxi_order.confirm_order()  # совершаем заказ

        taxi_order.wait_timer_ending()  # ожидаем поиск водителя

        header_text, header_status = taxi_order.get_order_header()
        # Проверка заголовка
        assert TorAndInterfaces.COMPLETION_HEADER in header_text
        assert header_status is True

        car_number_status, car_icon_status = taxi_order.get_car_info_status()
        # Проверка данных машины
        assert car_number_status is True
        assert car_icon_status is True

        name_status, avatar_status, rating_status = taxi_order.get_driver_info_status()
        # Проверка данных водителя
        assert name_status is True
        assert avatar_status is True
        assert rating_status is True

        cancel_btn, details_btn = taxi_order.get_order_setting_btn_status()
        # Проверка кнопок настройки заказа
        assert cancel_btn is True
        assert details_btn is True

    @allure.story('Проверка стоимости в деталях заказа')
    def test_taxi_order_flow_details(self, taxi_order):
        taxi_order.click_on_tariff('Рабочий')
        taxi_order.choose_laptop_table()
        price_from_preorder = taxi_order.get_active_tariff_price()

        taxi_order.confirm_order()  # совершаем заказ
        taxi_order.wait_timer_ending()  # ожидаем поиск водителя

        taxi_order.click_on_details()  # нажимаем на "детали"
        price_from_details = taxi_order.get_final_price()

        with allure.step('Данные теста'):
            allure.attach(str(price_from_preorder), name='price_from_preorder')
            allure.attach(str(price_from_details), name='price_from_details')

        # Проверка цены
        assert price_from_preorder == price_from_details

    @allure.story('Отмена заказа через кнопку "Отменить"')
    @pytest.mark.xfail(reason='Окно заказа, не закрывается по нажатию на кнопку Отмены')
    def test_taxi_order_flow_cancel(self, taxi_order):
        taxi_order.click_on_tariff('Рабочий')
        taxi_order.choose_laptop_table()
        taxi_order.confirm_order()  # совершаем заказ
        taxi_order.wait_timer_ending()  # ожидаем поиск водителя

        taxi_order.click_on_cancel()  # нажимаем на "отмена"

        try:
            taxi_order.wait_order_cancellation()
        except TimeoutException:
            allure.attach(
                taxi_order.get_screenshot(),
                name='window_not_closed',
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail('Окно заказа не закрылось после отмены')

        assert taxi_order.get_order_container_status() is False
