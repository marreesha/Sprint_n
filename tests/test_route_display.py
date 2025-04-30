import pytest
import allure
from src import TestParameters


@allure.feature('Отрисовка маршрута')
class TestRouteDisplay:

    @allure.story('Отображение точек маршрута на карте')
    @allure.title('Стартовая точка: {from_address}, Конечная точка: {to_address}')
    @pytest.mark.parametrize('from_address, to_address', TestParameters.TWO_ADDRESSES)
    def test_route_points_displayed(self, create_route, from_address, to_address):
        create_route.fill_from_field(from_address)
        create_route.fill_to_field(to_address)

        assert create_route.start_point_displayed() is True, 'Начальная точка не отображается'
        assert create_route.end_point_displayed() is True, 'Конечная точка не отображается'
