import allure

from src.ui.pages.base_page import BasePage
from src.ui.pages.home_page import HomePage

CART_PAGE_URL = 'https://www.demoblaze.com/prod.html'


class Locators:
    OPEN_CART = '//a[@class="nav-link" and text()="Cart"]'


class TopMenuElement:

    def __init__(self, page):
        self._base_page = BasePage(page, "")
        self.locators = Locators()

    @allure.step("Открытие страницы Корзины")
    def open_cart_page(self):
        self._base_page.page.click(self.locators.OPEN_CART)
