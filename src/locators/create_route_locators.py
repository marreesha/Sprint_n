from selenium.webdriver.common.by import By


class CreateRouteLocators:
    FROM_INPUT = (By.XPATH, '//input[@id="from"]')
    TO_INPUT = (By.XPATH, '//input[@id="to"]')

    START_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-0')]")
    END_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-1')]")
