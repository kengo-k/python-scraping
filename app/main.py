from playwright.sync_api import sync_playwright
from lib.arg import get_parser
from lib.get import exec as get

with sync_playwright() as playwright:
    parser = get_parser()
    args = parser.parse_args()
    value = get(playwright, args)
    print(value)