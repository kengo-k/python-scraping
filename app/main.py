from playwright.sync_api import sync_playwright
import src.test as lib

with sync_playwright() as playwright:
    page_url = "http://gitbucket.mynet/private/ssh/blob/master/install.sh"
    lib.run(playwright, page_url)