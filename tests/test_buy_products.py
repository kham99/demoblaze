import time

import allure
import pytest


@allure.feature("UI-тесты")
@pytest.mark.parametrize("category", ['phones',
                                      'laptops',
                                      'monitors'
                                      ])
def test_buy_product(page, home_page, cart_page, category):
    allure.dynamic.title(f"Добавление {category} в корзину")

    home_page.open()
    home_page.click_category(category)
    home_page.choice_product(category)

    product_name = home_page.get_product_name()
    cart_page.click_button_add_to_cart()
    cart_page.open()
    home_page.top_menu.open_cart_page()

    all_items = cart_page.get_all_items()
    with allure.step("Проверка наличия добавленного продукта в корзине"):
        assert product_name in all_items, "Товар не добавлен в корзину"
