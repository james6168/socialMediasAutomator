from playwright_engine.sync_browser import SyncBrowser
from instagram.models import Post, Image, History, HistorySlide


class Instagram:
    BROWSER = SyncBrowser()
    CREATE_BUTTON = "//span[text()='Создать']"
    PUBLICATION_SELECT = "//span[text()='Публикация']"
    PUBLICATION_FILE_UPLOAD_INPUT = "//form//input[@type='file']"
    PUBLICATION_NEXT_BUTTON = "//button[text()='Далее']"
    PUBLICATION_SHARE_BUTTON = "//div[@role='button' and text()='Поделиться']"
    
    def login(username, password):
        page = Instagram.BROWSER.new_page()
        page.goto('https://www.instagram.com/accounts/login/')
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.close()

    def close(self):
        Instagram.BROWSER.close()

    def create_publication(post: Post):
        page = Instagram.browser.new_page()
        page.goto('https://www.instagram.com/')
        page.click(Instagram.CREATE_BUTTON)
        page.click(Instagram.PUBLICATION_SELECT)
        page.fill(Instagram.PUBLICATION_FILE_UPLOAD_INPUT, post.image.image.path)
        page.click(Instagram.PUBLICATION_NEXT_BUTTON)
        page.click(Instagram.PUBLICATION_NEXT_BUTTON)
        if post.text:
            page.fill('textarea', post.text)
        
        page.click(Instagram.PUBLICATION_SHARE_BUTTON)
        page.close()