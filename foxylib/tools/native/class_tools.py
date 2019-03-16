import inspect
from operator import itemgetter as ig

from future.utils import lfilter

class ClassToolkit:
    @classmethod
    def cls2name(cls, clazz): return clazz.__name__

    @classmethod
    def cls2name_lower(cls, clazz): return cls.cls2name(clazz).lower()

class ModuleToolkit:
    @classmethod
    def module2class_list(cls, module):
        m_list = inspect.getmembers(module, inspect.isclass)
        clazz_list = lfilter(lambda x:x.__module__ == module.__name__, map(ig(1), m_list))
        return clazz_list
