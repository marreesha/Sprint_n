import allure
from .base_page import BasePage
from src.helpers import URLS, Addresses
from src.locators import CreateRouteLocators


class CreateRoutePage(BasePage):

    @allure.step("Переход на страницу «Яндекс Маршруты»")
    def get_main_page(self):
        self.get_page(URLS.BASE_URL)

    @allure.step("Заполнение поля «Откуда»")
    def fill_from_field(self, address=Addresses.ADDRESS_1):
        self.send_keys(CreateRouteLocators.FROM_INPUT, address)

    @allure.step("Заполнение поля «Куда»")
    def fill_to_field(self, address=Addresses.ADDRESS_2):
        self.send_keys(CreateRouteLocators.TO_INPUT, address)

    @allure.step("Получить стартовую точку маршрута")
    def start_point_displayed(self):
        return self.element_is_displayed(CreateRouteLocators.START_POINT)

    @allure.step("Получить конечную точку маршрута")
    def end_point_displayed(self):
        return self.element_is_displayed(CreateRouteLocators.END_POINT)
