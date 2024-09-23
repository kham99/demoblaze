import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()
