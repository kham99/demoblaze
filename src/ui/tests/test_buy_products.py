import logging
import time
import pytest
from playwright.sync_api import sync_playwright
from src.ui.pages.home_page import HomePage
from src.ui.pages.cart_page import CartPage
import allure

@allure.title("Добавление товара в корзину")
@allure.feature("UI-тесты")
@pytest.mark.parametrize("category", ['phones', 'laptops', 'monitors'])
def test_buy_product(page, category):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    home_page.open()
    home_page.click_category(category)
    home_page.choice_product(category)
    cart_page.click_button_add_to_cart()
    time.sleep(3)
