from l2l.templatetags.l2l_extras import format_datetime
from django.test import TestCase

import unittest
import re
from datetime import datetime

example_date_str = '2021-13T23:06:38'
example_date_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
example_error_1 = 'Not a date'
example_error_2 = 16

result_ex_str = format_datetime(example_date_str)
result_ex_datetime = format_datetime(example_date_datetime)
result_ex_datetime = format_datetime(example_error_1)
result_ex_datetime = format_datetime(example_error_2)

class Test_Date_Filter(unittest, TestCase):

  def test_date_type(self):

    self.assertEqual(type(result_ex_str), str)
    self.assertEqual(type(result_ex_datetime), str)
    self.assertEqual(type(example_error_1), str)
    self.assertEqual(type(example_error_2), str)

  def test_if_date_match(self):

    regex_str = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]"

    self.assertEqual(re.search(result_ex_str, regex_str), (0, 19))
    self.assertEqual(re.search(result_ex_datetime, regex_str), (0, 19))
    self.assertEqual(re.search(example_error_1, regex_str), (0, 19))
    self.assertEqual(re.search(example_error_2, regex_str), (0, 19))

