from playwright.sync_api import sync_playwright
from lib.arg import get_parser, validate_args, ResultCode
from lib.get import exec as get

def main():
  with sync_playwright() as playwright:
    parser = get_parser()
    args = parser.parse_args()
    (code, message) = validate_args(args)
    if (code is not ResultCode.SUCCESS):
      print(message)
      return
    value = get(playwright, args)
    print(value, end="")

if __name__ == '__main__':
  main()