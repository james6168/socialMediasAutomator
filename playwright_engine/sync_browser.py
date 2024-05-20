from playwright.sync_api import sync_playwright
from django.conf import settings


class SyncBrowser:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=settings.PLAYWRIGHT_HEADLESS
        )

    def new_page(self):
        page = self.browser.new_page()
        if settings.PLAYWRIGHT_FULLSCREEN:
            page.goto('about:blank')
            page.evaluate('''() => {
                document.documentElement.webkitRequestFullscreen()
            }''')
        return page

    def close(self):
        self.browser.close()
        self.playwright.stop()