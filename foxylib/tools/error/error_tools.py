from functools import wraps

from foxylib.tools.log.logger_tools import FoxylibLogger


class ErrorToolkit:
    @classmethod
    def log_when_error(cls, func=None, logger=None, err2msg=None,):
        if err2msg is None:
            err2msg = lambda e: 'Exception raised: {0}'.format(e)

        def wrapper(f):
            @wraps(f)
            def wrapped(*_, **__):
                _logger = logger if logger else FoxylibLogger.func2logger(f)

                try:
                    return f(*_, **__)
                except Exception as e:
                    _logger.exception(err2msg(e))
                    raise

            return wrapped

        return wrapper(func) if func else wrapper

    @classmethod
    def default_if_error(cls, func=None, default=None,):
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                try:
                    return f(*args,**kwargs)
                except Exception:
                    return default
            return wrapped

        return wrapper(func) if func else wrapper