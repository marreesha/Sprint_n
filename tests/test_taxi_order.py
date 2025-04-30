import pytest
import allure
from src import TorAndInterfaces, TestParameters, TaxiOrderPage


@allure.feature('Заказ тарифа Такси')
class TestTaxiOrder:

    @allure.story('Отображение формы заказа')
    def test_taxi_order_tariffs_check(self, driver, route_types):
        route_types.click_on_mode()
        route_types.click_on_taxi_button()
        page = TaxiOrderPage(driver)

        displayed_tariffs = page.get_displayed_tariffs()
        active_tariff = page.get_active_tariff()

        with allure.step('Данные теста'):
            allure.attach(str(displayed_tariffs), name='displayed_tariffs')
            allure.attach(str(active_tariff), name='active_tariff')

        assert displayed_tariffs == TorAndInterfaces.TARIFF_OPTIONS
        assert active_tariff in TorAndInterfaces.TARIFF_OPTIONS

    @allure.story('Отображение всплывающих подсказок тарифов')
    @allure.title('Тариф: {tariff}')
    @pytest.mark.parametrize('tariff', TestParameters.TAXI_TARIFF)
    def test_tariff_tooltips(self, taxi_order, tariff):
        taxi_order.click_on_tariff(tariff)
        taxi_order.move_cursor_to_icon()

        assert taxi_order.get_tooltip_state() is True

        title, text = taxi_order.get_tariff_information()

        with allure.step('Данные теста'):
            allure.attach(str(tariff), name='title_exp')
            allure.attach(str(title), name='title')
            allure.attach(str(TorAndInterfaces.TAXI_TARIFF_DESCRIPTION[tariff]), name='text_exp')
            allure.attach(str(text), name='text')

        assert title == tariff
        assert text == TorAndInterfaces.TAXI_TARIFF_DESCRIPTION[tariff]

    @allure.story('Отображение полей формы заказа')
    def test_order_form_fields(self, driver, route_types):
        route_types.click_on_mode()
        route_types.click_on_taxi_button()
        page = TaxiOrderPage(driver)

        displayed_fields = page.get_displayed_fields()

        with allure.step('Данные теста'):
            allure.attach(str(displayed_fields), name='displayed_fields')

        assert displayed_fields == TorAndInterfaces.TAXI_FIELDS_TO_FILL
