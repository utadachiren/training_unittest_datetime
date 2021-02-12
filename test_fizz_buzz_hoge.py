import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

# https://docs.python.org/ja/3/library/unittest.mock-examples.html#partial-mocking
# https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%812-%E7%B5%84%E3%81%BF%E8%BE%BC%E3%81%BF%E3%82%AF%E3%83%A9%E3%82%B9%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E9%96%A2%E6%95%B0%E3%81%AB%E4%BB%8B%E5%85%A5%E3%81%99%E3%82%8B

def fizz_buzz_hoge():
  now = datetime.now()
  if now.minute % 15 == 0:
    return 'Fizz'
  
  return 'Buzz'

class TestFizzBuzzHoge(unittest.TestCase):
  def test_15分の倍数でFizzを返す(self):
    with patch('test_fizz_buzz_hoge.datetime') as mock_datetime:
      mock_datetime.now.return_value = MagicMock(minute=30)
      expect = fizz_buzz_hoge()
      self.assertEqual('Fizz', expect)
  
  def test_18時以降の時はBuzzを返す(self):
    expect = fizz_buzz_hoge()
    self.assertEqual('Buzz', expect)