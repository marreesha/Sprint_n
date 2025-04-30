import allure
import re
from .base_page import BasePage
from src.helpers import TorAndInterfaces
from src.locators import TaxiOrderLocators


class TaxiOrderPage(BasePage):

    @allure.step("Получить видимые тарифы")
    def get_displayed_tariffs(self):
        states = {}
        for tariff in TorAndInterfaces.TARIFF_OPTIONS:
            states[tariff] = self.get_active_state(TaxiOrderLocators.TARIFF_LOCATOR(tariff))

        return self.check_active_items(states)

    @allure.step("Получить активный тариф")
    def get_active_tariff(self):
        active_tariffs = self.find_elements(TaxiOrderLocators.ACTIVE_TARIFF_TITLE)
        return self.get_active_item(active_tariffs)

    @allure.step("Получить видимые поля заказа")
    def get_displayed_fields(self):
        states = {}
        states['Телефон'] = self.get_active_state(TaxiOrderLocators.PHONE_FIELD)
        states['Способ оплаты'] = self.get_active_state(TaxiOrderLocators.PAYMENT_METHOD)
        states['Комментарий водителю'] = self.get_active_state(TaxiOrderLocators.COMMENT_FIELD)
        states['Требования к заказу'] = self.get_active_state(TaxiOrderLocators.REQUIREMENTS_SECTION)

        return self.check_active_items(states)

    @allure.step("Получить состояние всплывающего окна с деталями о тарифе")
    def get_tooltip_state(self):
        self.wait_for_element_to_be_visible(TaxiOrderLocators.ACTIVE_TOOLTIP)
        return self.get_active_state(TaxiOrderLocators.ACTIVE_TOOLTIP)

    @allure.step("Передвинуть курсор на 'i'")
    def move_cursor_to_icon(self):
        self.hover_over_element(TaxiOrderLocators.ACTIVE_TARIFF_I)

    @allure.step("Получить информацию о тарифе")
    def get_tariff_information(self):
        title = self.get_element_text(TaxiOrderLocators.ACTIVE_TOOLTIP_TITLE)
        text = self.get_element_text(TaxiOrderLocators.ACTIVE_TOOLTIP_DESCRIPTION)
        return title, text

    @allure.step("Выбрать тариф такси")
    def click_on_tariff(self, tariff='Рабочий'):
        locator = TaxiOrderLocators.TARIFF_LOCATOR(tariff)
        self.click_on(locator)

    @allure.step("Выбрать столик для ноутбука")
    def choose_laptop_table(self):
        self.click_on(TaxiOrderLocators.REQUIREMENTS_SECTION)
        self.click_on(TaxiOrderLocators.LAPTOP_TABLE_SWITCH)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on(TaxiOrderLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить статус кнопок управления заказом")
    def get_order_setting_btn_status(self):
        cancel = self.get_active_state(TaxiOrderLocators.CANCEL_BUTTON)
        details = self.get_active_state(TaxiOrderLocators.DETAILS_BUTTON)
        return cancel, details

    @allure.step("Получить поля окна ожидания")
    def get_waiting_status(self):
        self.wait_for_element_to_be_visible(TaxiOrderLocators.ORDER_WAITING_CONTAINER)
        title = self.get_element_text(TaxiOrderLocators.ORDER_HEADER_TITLE)
        timer_status = self.get_active_state(TaxiOrderLocators.ORDER_TIMER)
        return title, timer_status

    @allure.step("Ожидание заказа")
    def wait_timer_ending(self):
        self.wait_for_element_to_be_invisible(TaxiOrderLocators.ORDER_TIMER)

    @allure.step("Получить заголовок заказа")
    def get_order_header(self):
        text = self.get_element_text(TaxiOrderLocators.ORDER_HEADER)
        status = self.get_active_state(TaxiOrderLocators.ORDER_HEADER)
        return text, status

    @allure.step("Получить данные машины")
    def get_car_info_status(self):
        number = self.get_active_state(TaxiOrderLocators.CAR_NUMBER)
        icon = self.get_active_state(TaxiOrderLocators.CAR_ICON)
        return number, icon

    @allure.step("Получить данные водителя")
    def get_driver_info_status(self):
        name = self.get_active_state(TaxiOrderLocators.DRIVER_NAME)
        avatar = self.get_active_state(TaxiOrderLocators.DRIVER_AVATAR)
        rating = self.get_active_state(TaxiOrderLocators.DRIVER_RATING)
        return name, avatar, rating

    @allure.step("Клик по 'Детали'")
    def click_on_details(self):
        self.click_on(TaxiOrderLocators.DETAILS_BUTTON)

    @allure.step("Клик по 'Отмена'")
    def click_on_cancel(self):
        self.click_on(TaxiOrderLocators.CANCEL_BUTTON)

    def extract_number(self, text):
        match = re.search(r'\d+(?:[.,]\d+)?', text)
        if match:
            number_str = match.group().replace(',', '.')
            return float(number_str)
        return None

    @allure.step("Получить предварительную стоимость заказа")
    def get_active_tariff_price(self):
        price_text = self.get_element_text(TaxiOrderLocators.TARIFF_PRICE)
        return self.extract_number(price_text)

    @allure.step("Получить финальную стоимость заказа")
    def get_final_price(self):
        price_text = self.get_element_text(TaxiOrderLocators.ORDER_PRICE)
        return self.extract_number(price_text)

    @allure.step("Ожидание закрытия она заказа")
    def wait_order_cancellation(self):
        self.wait_for_element_to_be_invisible(TaxiOrderLocators.ORDER_WAITING_CONTAINER)

    @allure.step("Получить статус окна заказа")
    def get_order_container_status(self):
        return self.element_is_displayed(TaxiOrderLocators.ORDER_WAITING_CONTAINER)
