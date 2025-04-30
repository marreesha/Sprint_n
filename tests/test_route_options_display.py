import pytest
import allure
from src import TorAndInterfaces, TestParameters, RouteOptionsPage


@allure.feature('Отрисовка блока выбора маршрута')
class TestRouteOptionsDisplay:

    @allure.story('Отображение блока выбора маршрута')
    @allure.title('Стартовая точка: {from_address}, Конечная точка: {to_address}')
    @pytest.mark.parametrize('from_address, to_address', TestParameters.TWO_ADDRESSES)
    def test_route_options_displayed_two_adrs(self, driver, create_route, from_address, to_address):
        create_route.fill_from_field(from_address)
        create_route.fill_to_field(to_address)

        page = RouteOptionsPage(driver)
        displayed_modes = page.get_displayed_modes()

        with allure.step('Данные теста'):
            allure.attach(str(displayed_modes), name='displayed_modes')

        assert displayed_modes == TorAndInterfaces.ROUTE_MODES, 'Маршруты не соответствуют ТЗ'

    @allure.story('Отображение блока маршрута для одинакового адреса')
    @allure.title('Адрес: {address}')
    @pytest.mark.parametrize('address', TestParameters.ONE_ADDRESS)
    def test_route_options_displayed_one_adr(self, driver, create_route, address):
        create_route.fill_from_field(address)
        create_route.fill_to_field(address)

        page = RouteOptionsPage(driver)
        route_result = page.get_route_result()

        with allure.step('Данные теста'):
            allure.attach(str(route_result), name='route_result')

        assert route_result == TorAndInterfaces.ROUTE_RESULT_ONE_ADDRESS, 'Сообщение не соответствует ожидаемому'
