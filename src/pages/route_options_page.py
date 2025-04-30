import allure
from .base_page import BasePage
from src.helpers import TorAndInterfaces
from src.locators import RouteOptionsLocators


class RouteOptionsPage(BasePage):

    @allure.step("Получить стоимость и продолжительность маршрута")
    def get_route_result(self):
        self.wait_for_element_to_be_visible(RouteOptionsLocators.TEXT_RESULT_SEARCH)
        text = self.get_element_text(RouteOptionsLocators.TEXT_RESULT_SEARCH)
        duration = self.get_element_text(RouteOptionsLocators.DURATION_RESULT_SEARCH)
        return f'{text} {duration}'

    @allure.step("Выбор маршрута")
    def click_on_mode(self, mode='Быстрый'):
        locator = RouteOptionsLocators.MODE_LOCATOR(mode)
        return self.click_on(locator)

    @allure.step("Клик по кнопке «Драйв»")
    def click_on_drive(self):
        element = self.wait_for_element(RouteOptionsLocators.DRIVE_TRANSPORT)
        self.scroll_to_element(element)
        return self.click_on(RouteOptionsLocators.DRIVE_TRANSPORT)

    @allure.step("Клик по кнопке «Вызвать такси»")
    def click_on_taxi_button(self):
        self.click_on(RouteOptionsLocators.CALL_TAXI_BUTTON)

    @allure.step("Получить статус кнопки «Вызвать такси»")
    def taxi_button_is_active(self):
        return self.get_active_state(RouteOptionsLocators.CALL_TAXI_BUTTON)

    @allure.step("Получить статус кнопки «Забронировать»")
    def book_button_is_active(self):
        return self.get_active_state(RouteOptionsLocators.BOOK_BUTTON)

    @allure.step("Получить отображаемые варианты маршрута")
    def get_displayed_modes(self):
        states = {}
        for mode in TorAndInterfaces.ROUTE_MODES:
            locator = RouteOptionsLocators.MODE_LOCATOR(mode)
            states[mode] = self.get_active_state(locator)

        return self.check_active_items(states)

    @allure.step("Получить активный вариант маршрута")
    def get_active_mode(self):
        active_modes = self.find_elements(RouteOptionsLocators.ACTIVE_MODE)
        return self.get_active_item(active_modes)

    @allure.step("Получить отображаемые варианты транспорта")
    def get_displayed_transport(self):
        states = {}
        for transport in TorAndInterfaces.MOVEMENT_OPTIONS:
            locator = RouteOptionsLocators.TRANSPORT_LOCATOR(transport)
            states[transport] = self.get_active_state(locator)

        return self.check_active_items(states)
