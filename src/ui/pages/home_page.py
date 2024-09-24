import random
from enum import StrEnum

import allure

from src.ui.pages.base_page import BasePage
from src.ui.pages.elements.top_menu import TopMenuElement

HOME_PAGE_URL = 'https://www.demoblaze.com/index.html'


class Good(StrEnum):
    NEXUS_6 = "Nexus 6"


class HomePageLocators:
    PHONES_CATEGORY = """//a[@onclick = "byCat('phone')"]"""
    LAPTOPS_CATEGORY = """//a[@onclick = "byCat('notebook')"]"""
    MONITORS_CATEGORY = """//a[@onclick = "byCat('monitor')"]"""
    PHONE_NEXUS_6 = '//div//a[@href="prod.html?idp_=3"]'
    PHONE_GALAXY_S6 = '//div//a[@href="prod.html?idp_=1"]'
    PHONE_GALAXY_S7 = '//div//a[@href="prod.html?idp_=4"]'
    PHONE_NOKIA_LUMIA = '//div//a[@href="prod.html?idp_=2"]'
    PHONE_IPHONE_6 = '//div//a[@href="prod.html?idp_=5"]'
    PHONE_SONY_XPERIA = '//div//a[@href="prod.html?idp_=6"]'
    PHONE_HTC = '//div//a[@href="prod.html?idp_=7"]'
    LAPTOP_SONY_VAIO_I7 = '//div//a[@href="prod.html?idp_=8"]'
    LAPTOP_SONY_VAIO_I5 = '//div//a[@href="prod.html?idp_=9"]'
    LAPTOP_MACBOOK_AIR = '//div//a[@href="prod.html?idp_=11"]'
    LAPTOP_MACBOOK_PRO = '//div//a[@href="prod.html?idp_=15"]'
    LAPTOP_DELL_I7 = '//div//a[@href="prod.html?idp_=12"]'
    LAPTOP_DELL_2017 = '//div//a[@href="prod.html?idp_=13"]'
    MONITOR_APPLE = '//div//a[@href="prod.html?idp_=10"]'
    MONITOR_ASUS = '//div//a[@href="prod.html?idp_=14"]'
    ALL_PHONES_LOCATORS = [PHONE_NEXUS_6, PHONE_GALAXY_S6, PHONE_NOKIA_LUMIA, PHONE_IPHONE_6,
                           PHONE_SONY_XPERIA, PHONE_HTC]
    ALL_LAPTOPS_LOCATORS = [LAPTOP_SONY_VAIO_I5, LAPTOP_SONY_VAIO_I7, LAPTOP_MACBOOK_PRO, LAPTOP_MACBOOK_AIR,
                            LAPTOP_DELL_I7, LAPTOP_DELL_2017]
    ALL_MONITORS_LOCATORS = [MONITOR_ASUS, MONITOR_APPLE]

    PRODUCT_NAME = '//h2[@class="name"]'



    @staticmethod
    def locator(good_text: Good) -> str:
        return f"//a[@class='hrefch' and text()='{good_text}']"


class HomePage:
    url = HOME_PAGE_URL

    def __init__(self, page):
        self._base_page = BasePage(page, self.url)
        self.locators = HomePageLocators()
        self.top_menu = TopMenuElement(page)

    @allure.step("Открытие домашней страницы")
    def open(self):
        self._base_page.open()

    @allure.step("Клик по категории {category}")
    def click_category(self, category):
        with allure.step("Контекстный менеджер"):
            if category == 'phones':
                self._base_page.click(self.locators.PHONES_CATEGORY)
            elif category == 'monitors':
                self._base_page.click(self.locators.MONITORS_CATEGORY)
            elif category == 'laptops':
                self._base_page.click(self.locators.LAPTOPS_CATEGORY)

    def add_good(self, good: Good):
        locator = self.locators.locator(good)
        self._base_page.click(locator)

    def choice_product(self, category):
        if category == 'phones':
            random_locator = random.choice(self.locators.ALL_PHONES_LOCATORS)
            self._base_page.page.click(random_locator)
        elif category == 'monitors':
            random_locator = random.choice(self.locators.ALL_MONITORS_LOCATORS)
            self._base_page.page.click(random_locator)
        elif category == 'laptops':
            random_locator = random.choice(self.locators.ALL_LAPTOPS_LOCATORS)
            self._base_page.page.click(random_locator)

    @allure.step("Получение названия продукта")
    def get_product_name(self):
        return self._base_page.get_text(locator=self.locators.PRODUCT_NAME)


