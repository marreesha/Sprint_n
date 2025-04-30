from selenium.webdriver.common.by import By


class RouteOptionsLocators:
    # Режимы поиска
    ACTIVE_MODE = (By.CSS_SELECTOR, ".modes-container .mode.active")
    MODE_LOCATOR = lambda mode: (By.XPATH, f"//div[contains(@class, 'mode') and text()='{mode}']")

    # Результат (цена/время в пути)
    TEXT_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='text']")
    DURATION_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='duration']")

    # Типы транспорта
    ACTIVE_TRANSPORT = (By.CSS_SELECTOR, ".types-container .type.active")
    TRANSPORT_LOCATOR = lambda transport: (By.CSS_SELECTOR, f".type img[src*='{transport}']")
    DRIVE_TRANSPORT = (By.XPATH, "//div[@class = 'type drive']")

    # Такси
    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Вызвать такси']")

    # Драйв
    BOOK_BUTTON = (By.XPATH, "//button[text()='Забронировать']")
