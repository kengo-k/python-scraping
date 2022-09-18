import urllib.request
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

def run(playwright, page_url):

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    page.goto(page_url)

    raw_button_loc = page.locator('text=RAW')
    raw_link = raw_button_loc.get_attribute('href')

    parsed_url = urlparse(page_url)
    scheme = parsed_url.scheme
    domain = parsed_url.netloc
    if (raw_link[0] == '/'):
        print(f'{scheme}://{domain}{raw_link}')
    else:
        print(raw_link)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    page_url = "http://gitbucket.mynet/private/ssh/blob/master/install.sh"
    run(playwright, page_url)