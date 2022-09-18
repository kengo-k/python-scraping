import urllib.request
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

def exec(playwright, args):

  browser = playwright.chromium.launch(headless=True)
  context = browser.new_context()

  page = context.new_page()
  page.goto(args.url)

  loc = page.locator(args.selector)
  value = None
  if (args.content):
    value = loc.inner_text()
  else:
    value = loc.get_attribute(args.attribute)

  context.close()
  browser.close()

  return value