import unittest
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

from lib.arg import get_parser
from lib.get import exec as get

HOST = "localhost"
PORT = 3000
URL = f"http://{HOST}:{PORT}/test.html"

class Server(HTTPServer):
  def run(self):
    try:
      self.serve_forever()
    except KeyboardInterrupt:
      pass
    finally:
      self.server_close()

class TestGet(unittest.TestCase):

  def setUp(self):
    self.server = Server((HOST, PORT), SimpleHTTPRequestHandler)
    self.thread = threading.Thread(None, self.server.run)
    self.thread.start()
    self.parser = get_parser()

  def tearDown(self):
    self.server.shutdown()
    self.thread.join()

  def test_attribute(self):
    with sync_playwright() as playwright:
      args = self.parser.parse_args([URL,  "a[id='link1']", '-a', 'href'])
      result = get(playwright, args)
      self.assertEqual(result, "/foo.html")

  def test_attribute_by_content(self):
    with sync_playwright() as playwright:
      args = self.parser.parse_args([URL,  "a:has-text('foo')", '-a', 'href'])
      result = get(playwright, args)
      self.assertEqual(result, "/foo.html")

  def test_content(self):
    with sync_playwright() as playwright:
      args = self.parser.parse_args([URL,  "a[id='link1']", '-c'])
      result = get(playwright, args)
      self.assertEqual(result, "foo")