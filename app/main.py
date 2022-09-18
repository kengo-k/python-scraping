from playwright.sync_api import sync_playwright
import lib.get as get

with sync_playwright() as playwright:
    page_url = "http://gitbucket.mynet/private/ssh/blob/master/install.sh"
    get.run(playwright, page_url)