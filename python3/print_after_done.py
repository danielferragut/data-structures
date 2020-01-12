from functools import wraps

def print_after_done(method):
     @wraps(method)
     def _impl(self, *method_args, **method_kwargs):
         method_output = method(self, *method_args, **method_kwargs)
         print(self)
         return method_output
     return _impl
