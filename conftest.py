import pytest
from playwright.sync_api import sync_playwright

from src.ui.pages.cart_page import CartPage
from src.ui.pages.home_page import HomePage
from src.ui.pages.good_page import GoodPage


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()


@pytest.fixture()
def home_page(page) -> HomePage:
    return HomePage(page)


@pytest.fixture()
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture()
def good_page(page) -> GoodPage:
    return GoodPage(page)
