import functools
from functools import wraps

def log_activity(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
            result = function(*args **kwargs )
            return result
      return wrapper 