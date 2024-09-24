import allure

from src.ui.pages.base_page import BasePage
from src.ui.pages.home_page import HomePage

CART_PAGE_URL = 'https://www.demoblaze.com/prod.html'


class CartPageLocators:
    ADD_TO_CART_BUTTON = '//div//a[@class="btn btn-success btn-lg"]'
    OPEN_CART = '//a[@class="nav-link" and text()="Cart"]'
    CART_ITEMS = '//tr[@class="success"]/td[2]'


class CartPage:
    url = CART_PAGE_URL

    def __init__(self, page):
        self._base_page = BasePage(page, self.url)
        self._home_page = HomePage(page)
        self.locators = CartPageLocators()

    @allure.step("Открытие страницы Корзины")
    def open(self):
        self._base_page.page.click(self.locators.OPEN_CART)

    @allure.step("Клик по кнопке Добавить в корзину")
    def click_button_add_to_cart(self):
        self._base_page.click(self.locators.ADD_TO_CART_BUTTON)

    @allure.step("Получение списка товаров в корзине")
    def get_all_items(self) -> list[str]:
        return self._base_page.get_text_for_elements(self.locators.CART_ITEMS)

    # def expect_phone(self):
    #     locator = self._base_page.page.locator("td.name")
    #     expect(locator).to_have_text(self.phone_name)
