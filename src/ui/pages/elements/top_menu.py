import allure
from src.ui.pages.base_page import BasePage

CART_PAGE_URL = 'https://www.demoblaze.com/prod.html'


class TopMenuLocators:
    OPEN_HOME = '//a[@class="nav-link" and @href="index.html"]'
    OPEN_CART = '//a[@class="nav-link" and text()="Cart"]'
    OPEN_CONTACT = '//a[@class="nav-link" and text()="Contact"]'
    OPEN_ABOUT_US = '//a[@class="nav-link" and text()="About us"]'
    OPEN_LOG_IN = '//a[@class="nav-link" and text()="Log in"]'
    OPEN_SIGN_UP = '//a[@class="nav-link" and text()="Sign up"]'


class TopMenuElement:

    def __init__(self, page):
        self._base_page = BasePage(page, "")
        self.locators = TopMenuLocators()

    @allure.step("Открытие страницы Корзины")
    def open_cart_page(self):
        self._base_page.page.click(self.locators.OPEN_CART)

    @allure.step("Открытие домашней страницы")
    def open_home_page(self):
        self._base_page.page.click(self.locators.OPEN_HOME)

    @allure.step("Открытие формы обратной связи")
    def open_contact_page(self):
        self._base_page.page.click(self.locators.OPEN_CONTACT)

    @allure.step('Открытие страницы "О нас"')
    def open_about_us_page(self):
        self._base_page.page.click(self.locators.OPEN_ABOUT_US)

    @allure.step("Открытие страницы регистрации")
    def open_sign_up_page(self):
        self._base_page.page.click(self.locators.OPEN_SIGN_UP)

    @allure.step("Открытие страницы авторизации")
    def open_log_in_page(self):
        self._base_page.page.click(self.locators.OPEN_LOG_IN)
