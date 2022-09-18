import urllib.request
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

def exec(playwright, args):

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    page.goto(args.url)

    raw_button_loc = page.locator(args.selector)
    raw_link = raw_button_loc.get_attribute(args.attribute)

    print(raw_link)

    context.close()
    browser.close()