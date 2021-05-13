from datetime import datetime
from django import template
from datetime import datetime

register = template.Library()

# The l2l_extras template tag and the l2l_dt filter names are what we used in creating the exercise. Your filter needs to handle receiving a date object and a string.
#
# The string format will be in the following format: "%Y-%m-%dT%H:%M:%S".
#
#
#
# You will know you have succeeded when you can hit the main web page after removing the comments on lines 60 and 61 and the browser shows the results accurately.


# Your filter should print the results in the following format: "%Y-%m-%d %H:%M:%S".
def format_datetime(date_param):
  if type(date_param) == str:
    return format_str(date_param)
  elif type(date_param) == datetime:
    return format_datetime_obj(date_param)
  else:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_str(date_str):
  str_to_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
  formatted_datetime = str_to_datetime.strftime("%Y-%m-%d %H:%M:%S")
  return formatted_datetime

def format_datetime_obj(datetime_object):
  formatted_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
  return formatted_datetime

register.filter('format_datetime', format_datetime)
