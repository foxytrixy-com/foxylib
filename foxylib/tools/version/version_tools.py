import warnings
from functools import wraps

from future.utils import lmap
from nose.tools import assert_greater

from foxylib.tools.string.string_tools import str2lower


class VersionToolkit:
    @classmethod
    def _strip_prefix_v(cls, v):
        if not v: return v
        if str2lower(v[0]) != "v": return v

        return v[1:]

    @classmethod
    def version_str2int_list(cls, v):
        s = cls._strip_prefix_v(v)
        l = lmap(int, s.split("."))
        return l

    @classmethod
    def compare(cls, v1, v2):
        l1,l2 = lmap(cls.version_str2int_list, [v1,v2])

        n = max(len(l1), len(l2))

        for i in range(n):
            if i >= len(l1): return -1
            if i >= len(l2): return 1

            if l1[i] < l2[i]: return -1
            if l1[i] > l2[i]: return 1

        return 0

    @classmethod
    def version2parent(cls, v):
        l = v.split(".")
        assert_greater(len(l), 1)

        return ".".join(l[:-1])


    class CheckBeforeRunError(Exception):
        pass

    @classmethod
    def check_before_use(cls, func=None, reason=None):
        def _wrapper(f_IN):
            @wraps(f_IN)
            def wrapped(*args, **kwargs):
                raise cls.CheckBeforeRunError(reason)

            return wrapped

        if func is None:
            return _wrapper
        else:
            return _wrapper(func)


    class NotWorkingError(Exception):
        pass

    @classmethod
    def not_working(cls, func=None, reason=None):
        def _wrapper(f_IN):
            @wraps(f_IN)
            def wrapped(*args, **kwargs):
                raise cls.NotWorkingError(reason)

            return wrapped

        if func is None:
            return _wrapper
        else:
            return _wrapper(func)

    class RemovedError(Exception):
        pass

    @classmethod
    def removed(cls, func=None, reason=None):
        def _wrapper(f_IN):
            @wraps(f_IN)
            def wrapped(*args, **kwargs):
                raise cls.RemovedError(reason)

            return wrapped

        if func is None:
            return _wrapper
        else:
            return _wrapper(func)

    class DeprecatedError(Exception):
        pass

    @classmethod
    def deprecated(cls, func=None, version_current=None, version_tos=None, reason=None):
        def _wrapper(f_IN):
            @wraps(f_IN)
            def wrapped(*args, **kwargs):
                if cls.compare(version_current,version_tos)>=0:
                    raise cls.DeprecatedError(reason)

                warnings.simplefilter('always', DeprecationWarning)  # turn off filter
                warnings.warn("Call to deprecated function {}.".format(func.__name__),
                              category=DeprecationWarning,
                              stacklevel=2)
                warnings.simplefilter('default', DeprecationWarning)  # reset filter
                return func(*args, **kwargs)

            return wrapped

        if func is None:
            return _wrapper
        else:
            return _wrapper(func)