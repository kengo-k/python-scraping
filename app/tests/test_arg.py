from lib.arg import get_parser, validate_args, ResultCode
import unittest

url = 'http://foo.com'
selector = 'div'

class TestArg(unittest.TestCase):

  def test_valid(self):
    parser = get_parser()
    args = parser.parse_args([url, selector, '--a', 'href'])
    (code, message) = validate_args(args)
    self.assertEqual(code, ResultCode.SUCCESS)
    self.assertIsNone(message)

  def test_valid2(self):
    parser = get_parser()
    args = parser.parse_args([url, selector, '--c'])
    (code, message) = validate_args(args)
    self.assertEqual(code, ResultCode.SUCCESS)

  def test_invalid(self):
    parser = get_parser()
    args = parser.parse_args([url, selector])
    (code, message) = validate_args(args)
    self.assertEqual(code, ResultCode.E0001)
    self.assertIsNotNone(message)

  def test_invalid2(self):
    parser = get_parser()
    args = parser.parse_args([url, selector, '--a=href','--c'])
    (code, message) = validate_args(args)
    self.assertEqual(code, ResultCode.E0002)
    self.assertIsNotNone(message)

  def test_attribute(self):
    parser = get_parser()
    args = [url, selector, '--attribute', 'href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')
    self.assertEqual(result.selector, selector)
    self.assertFalse(result.content)
    self.assertEqual(result.url, url)

  def test_attribute2(self):
    parser = get_parser()
    args = [url, selector, '--attribute=href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')

  def test_attribute_short(self):
    parser = get_parser()
    args = [url,  selector, '-a', 'href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')

  def test_attribute_short2(self):
    parser = get_parser()
    args = [url,  selector, '-a=href']
    result = parser.parse_args(args)
    self.assertEqual(result.attribute, 'href')