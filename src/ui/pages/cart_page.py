from src.ui.pages.base_page import BasePage
from src.ui.pages.home_page import HomePage
from playwright.sync_api import expect

CART_PAGE_URL = 'https://www.demoblaze.com/prod.html'

class CartPageLocators:
    ADD_TO_CART_BUTTON = '//div//a[@class="btn btn-success btn-lg"]'

class CartPage:
    url = CART_PAGE_URL

    def __init__(self, page):
        self._base_page = BasePage(page, self.url)
        self._home_page = HomePage(page)
        self.locators = CartPageLocators()


    def open(self):
        self._base_page.open()

    def click_button_add_to_cart(self):
        self._base_page.click(self.locators.ADD_TO_CART_BUTTON)

    # def expect_phone(self):
    #     locator = self._base_page.page.locator("td.name")
    #     expect(locator).to_have_text(self.phone_name)



