import pytest
from selenium import webdriver
from src import CreateRoutePage, RouteOptionsPage, TaxiOrderPage


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def create_route(driver):
    page = CreateRoutePage(driver)
    page.get_main_page()
    return page


@pytest.fixture()
def route_types(driver, create_route):
    create_route.fill_from_field()
    create_route.fill_to_field()
    page = RouteOptionsPage(driver)
    return page


@pytest.fixture()
def taxi_order(driver, route_types):
    route_types.click_on_mode()
    route_types.click_on_taxi_button()
    page = TaxiOrderPage(driver)
    return page
