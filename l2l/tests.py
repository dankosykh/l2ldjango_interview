from l2l.templatetags.l2l_extras import format_datetime
from django.test import TestCase

import re
from datetime import datetime

example_date_str = '2021-05-14T00:24:58'
example_date_datetime = datetime.now()
example_error_1 = 'Not a date'
example_error_2 = 16

result_ex_str = format_datetime(example_date_str)
result_ex_datetime = format_datetime(example_date_datetime)
result_ex_error_1 = format_datetime(example_error_1)
result_ex_error_2 = format_datetime(example_error_2)

class Test_Date_Filter(TestCase):

  def test_date_type(self):

    self.assertEqual(type(result_ex_str), str)
    self.assertEqual(type(result_ex_datetime), str)
    self.assertEqual(type(result_ex_error_1), str)
    self.assertEqual(type(result_ex_error_2), str)

  def test_if_date_formatted(self):

    regex_str = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]"

    self.assertEqual(re.search(regex_str, result_ex_str).span(), (0, 19))
    self.assertEqual(re.search(regex_str, result_ex_datetime).span(), (0, 19))
    self.assertEqual(re.search(regex_str, result_ex_error_1).span(), (0, 19))
    self.assertEqual(re.search(regex_str, result_ex_error_2).span(), (0, 19))
