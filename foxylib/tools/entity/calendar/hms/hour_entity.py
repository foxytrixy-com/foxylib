from functools import lru_cache

from foxylib.tools.entity.entity_tool import FoxylibEntity
from foxylib.tools.function.function_tool import FunctionTool


class HourEntity:
    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def entity_type(cls):
        return FoxylibEntity.class2entity_type(cls)
