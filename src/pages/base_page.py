from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.__timeout = timeout
        self.wait = WebDriverWait(self.driver, self.__timeout)

    def set_timeout(self, timeout):
        self.__timeout = timeout

    def find_element(self, locator):
        """Метод для поиска элемента на странице"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Метод для поиска множества элементов"""
        return self.driver.find_elements(*locator)

    def click_on(self, locator):
        """Метод для клика по элементу"""
        _element = self.wait_for_element_to_be_clickable(locator)
        _element.click()

    def send_keys(self, locator, text):
        """Метод для ввода текста в поле"""
        _element = self.find_element(locator)
        _element.clear()  # Очищаем поле перед вводом
        _element.send_keys(text)

    def wait_for_page(self, url):
        """Метод ожидания появления страницы"""
        return self.wait.until(EC.url_to_be(url))

    def wait_for_element(self, locator):
        """Метод ожидания появления элемента на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Метод ожидания, чтобы элемент стал кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        """Метод ожидания видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator):
        """Метод ожидания невидимости элемента"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def scroll_to_element(self, element):
        """Метод прокрутки страницы до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self.wait.until(EC.visibility_of(element))

    def scroll_to(self, locator):
        """Метод прокрутки страницы до элемента"""
        _element = self.find_element(locator)
        return self.scroll_to_element(_element)

    def get_page(self, url):
        """Метод вызова и ожидания загрузки страницы"""
        self.driver.get(url)
        self.wait_for_page(url)

    def click_on_with_execute_script(self, locator):
        """Метод для клика по элементу"""
        _element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", _element)

    def drag_ingredient_to_order(self, source, target):
        """Метод для выполнения перетаскивания"""
        # Используем JavaScript для выполнения перетаскивания
        js_drag_and_drop = """
                    const ingredient = arguments[0];
                    const orderSection = arguments[1];

                    // Создаем события для перетаскивания
                    const dragStartEvent = new DragEvent('dragstart', { bubbles: true });
                    const dragOverEvent = new DragEvent('dragover', { bubbles: true });
                    const dropEvent = new DragEvent('drop', { bubbles: true });

                    // Инициируем начало перетаскивания
                    ingredient.dispatchEvent(dragStartEvent);

                    // Перетаскиваем в область заказа
                    orderSection.dispatchEvent(dragOverEvent);
                    orderSection.dispatchEvent(dropEvent);
                """
        self.driver.execute_script(js_drag_and_drop, source, target)

    def get_current_url(self):
        """Метод для извлечения текущего url"""
        return self.driver.current_url

    def wait_for_close_element(self, locator):
        """Метод ожидания исчезновения элемента"""
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    def make_element_visible(self, locator):
        _element = self.find_element(locator)
        self.driver.execute_script("arguments[0].style.display = 'block';", _element)

    def wait_for_url_matches(self, pattern):
        return self.wait.until(EC.url_matches(pattern))

    def element_is_displayed(self, locator):
        _element = self.wait_for_element_to_be_visible(locator)
        return _element.is_displayed()

    def get_element_text(self, locator):
        _element = self.find_element(locator)
        return _element.text

    def get_attribute_class(self, locator):
        _element = self.find_element(locator)
        return _element.get_attribute('class')

    def get_active_state(self, locator):
        _element = self.wait_for_element_to_be_visible(locator)
        return _element.is_displayed() and _element.is_enabled()

    def hover_over_element(self, locator):
        """Метод для перемещения курсора"""
        _element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(_element).perform()

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()

    def check_active_items(self, states):
        return set(k for k, v in states.items() if v)

    def get_active_item(self, active_items):
        if len(active_items) == 1:
            return active_items[0].text
        elif 1 < len(active_items):
            return 'multiple'
        else:
            return None
