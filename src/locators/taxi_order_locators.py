from selenium.webdriver.common.by import By


class TaxiOrderLocators:
    # Локаторы для тарифов
    ACTIVE_TARIFF_TITLE = (By.CSS_SELECTOR, ".tariff-cards .tcard.active .tcard-title")
    ACTIVE_TARIFF_I = (By.CSS_SELECTOR, ".tariff-cards .tcard.active .tcard-i")

    TARIFF_LOCATOR = lambda tariff: (By.XPATH, f"//div[contains(@class, 'tcard') and .//div[text()='{tariff}']]")

    # Поля заказа
    PHONE_FIELD = (By.XPATH, "//div[contains(text(), 'Телефон')]")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'pp-button') and .//div[contains(text(), 'Способ оплаты')]]")
    COMMENT_FIELD = (By.XPATH, "//input[@id='comment']")
    REQUIREMENTS_SECTION = (By.XPATH, "//div[contains(@class, 'reqs-header')]")
    LAPTOP_TABLE_SWITCH = (
        By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Столик для ноутбука']/following-sibling::div//span")

    # Информация о тарифе
    ACTIVE_TOOLTIP = (By.XPATH,
                      "//div[contains(@class, 'tcard active')]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    ACTIVE_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(@class, 'i-title')]")
    ACTIVE_TOOLTIP_DESCRIPTION = (By.XPATH,
                                  "//div[contains(@class, 'tcard active')]//div[contains(@class, 'i-dPrefix')]")

    # Подтверждение заказа
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button-main")

    # Ожидание такси
    ORDER_WAITING_CONTAINER = (By.CSS_SELECTOR, ".order-body")
    ORDER_HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    ORDER_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    ORDER_PROGRESS_BAR = (By.CSS_SELECTOR, ".order-progress")

    # Шапка заказа
    ORDER_HEADER = (By.CSS_SELECTOR, ".order-header")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    CAR_ICON = (By.CSS_SELECTOR, ".order-number img[alt='Car']")

    # Кнопки управления
    CANCEL_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]")
    CANCEL_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]/following-sibling::div")  # "Отменить"

    DETAILS_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]")
    DETAILS_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]/following-sibling::div")  # "Детали"

    # Информация о водителе
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")  # "4,9"
    DRIVER_NAME = (By.XPATH,
                   "//div[contains(@class, 'order-btn-group') and .//div[contains(@class, 'order-btn-rating')]]/following-sibling::div")
    DRIVER_AVATAR = (By.CSS_SELECTOR, "img[alt='close']")

    # Стоимость поездки по тарифу
    TARIFF_PRICE = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(@class, 'tcard-price')]")
    ORDER_PRICE = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")
