import allure
import pytest


@allure.feature("UI-тесты")
@pytest.mark.parametrize("category", ['phones',
                                      'laptops',
                                      'monitors'
                                      ])
def test_buy_product(page, home_page, good_page, cart_page, category):
    allure.dynamic.title(f"Добавление {category} в корзину")

    home_page.open()
    home_page.click_category(category)
    home_page.choice_product(category)

    product_name = home_page.get_product_name()
    product_price = home_page.get_price_product()
    good_page.click_button_add_to_cart()
    cart_page.open()

    formatted_product_price = home_page.extract_number(product_price)
    formatted_price_items = [home_page.extract_number(price) for price in cart_page.get_all_price_items()]
    all_items_cart = cart_page.get_all_items()

    with allure.step("Проверка наличия добавленного продукта в корзине"):
        assert product_name in all_items_cart, "Товар не добавлен в корзину"
    with allure.step("Проверка соответствия цены добавленного продукта в корзине"):
        assert formatted_product_price in formatted_price_items, "Цена товара в корзине не соответвует цене товара на главной странице"
