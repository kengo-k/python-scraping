import lib.arg as arg
import unittest

url = 'http://foo.com'
selector = 'div'

class TestArg(unittest.TestCase):

  def test_attribute(self):
    parser = arg.get_parser()
    args = [url, selector, '--attribute', 'href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')
    self.assertEqual(result.selector, selector)
    self.assertFalse(result.content)
    self.assertEqual(result.url, url)

  def test_attribute2(self):
    parser = arg.get_parser()
    args = [url, selector, '--attribute=href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')

  def test_attribute_short(self):
    parser = arg.get_parser()
    args = [url,  selector, '-a', 'href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')

  def test_attribute_short2(self):
    parser = arg.get_parser()
    args = [url,  selector, '-a=href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')