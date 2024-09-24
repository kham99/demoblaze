from playwright.sync_api import Page, Locator

import allure

DEFAULT_TIMEOUT = 5000

class BasePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    @allure.step("Открытие страницы")
    def open(self):
        self.page.goto(self.url)

    def _get_locator(self, locator: str, timeout: int = DEFAULT_TIMEOUT) -> Locator:
        locator = self.page.locator(locator)
        locator.wait_for(state="visible", timeout=timeout)
        return locator

    @allure.step("Клик по локатору {locator}")
    def click(self, locator):
        self._get_locator(locator).click()

    @allure.step("Получение текста по локатору {locator}")
    def get_text(self, locator: str) -> str:
        return self._get_locator(locator).text_content()

    def get_text_for_elements(self, locator: str) -> list[str]:
        return [text.replace('\n', '').replace("\t", "") for text in self._get_locator(locator).all_inner_texts()]
