import allure

from src.ui.pages.base_page import BasePage
from src.ui.pages.home_page import HomePage
from src.ui.pages.elements.top_menu import TopMenuLocators

CART_PAGE_URL = 'https://www.demoblaze.com/cart.html'


class CartPageLocators:
    OPEN_CART = '//a[@class="nav-link" and text()="Cart"]'
    CART_ITEMS = '//tr[@class="success"]/td[2]'
    PRICE_ITEMS = '//tr[@class="success"]/td[3]'


class CartPage:
    url = CART_PAGE_URL

    def __init__(self, page):
        self._base_page = BasePage(page, self.url)
        self._home_page = HomePage(page)
        self.locators = CartPageLocators()
        self.locators_top_menu = TopMenuLocators()

    @allure.step("Открытие страницы Корзины")
    def open(self):
        self._base_page.page.click(self.locators.OPEN_CART)

    @allure.step("Получение списка товаров в корзине")
    def get_all_items(self) -> list[str]:
        return self._base_page.get_text_for_elements(self.locators.CART_ITEMS)

    @allure.step("Получение цен товаров из корзины")
    def get_all_price_items(self) -> list[str]:
        return self._base_page.get_text_for_elements(self.locators.PRICE_ITEMS)
