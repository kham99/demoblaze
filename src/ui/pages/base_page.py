from playwright.sync_api import Page



class BasePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def click(self, locator):
        self.page.click(locator)

