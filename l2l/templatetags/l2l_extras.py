from datetime import datetime
from django import template
from datetime import datetime

register = template.Library()

# Your filter should print the results in the following format: "%Y-%m-%d %H:%M:%S".
def format_datetime(date_param):
  if type(date_param) == str:
    return format_str(date_param)
  elif type(date_param) == datetime:
    return format_datetime_obj(date_param)
  else:
    return fallback_date()

# if date is string
def format_str(date_str):
  try:
    str_to_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    formatted_datetime = str_to_datetime.strftime("%Y-%m-%d %H:%M:%S")
  except:
    formatted_datetime = fallback_date()
  return formatted_datetime

# if date is datetime object
def format_datetime_obj(datetime_object):
  formatted_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
  return formatted_datetime

# if all else fails
def fallback_date():
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

register.filter('format_datetime', format_datetime)
