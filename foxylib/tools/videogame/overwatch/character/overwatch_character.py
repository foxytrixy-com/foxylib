import os
from functools import lru_cache

from foxylib.tools.collections.collections_tool import filter2singleton
from foxylib.tools.function.function_tool import FunctionTool
from foxylib.tools.json.json_tool import jdown
from foxylib.tools.json.yaml_tool import YAMLTool

FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)

class OverwatchCharacter:
    class Codename:
        DVA = "dva"
        ORISA = "orisa"
        REINHARDT = "reinhardt"
        ROADHOG = "roadhog"
        SIGMA = "sigma"
        WINSTON = "winston"
        WRECKINGbALL = "wreckingball"
        ZARYA = "zarya"
        ANA = "ana"
        BAPTISTE = "baptiste"
        BRIGITTE = "brigitte"
        LUCIO = "lucio"
        MERCY = "mercy"
        MOIRA = "moira"
        ZENYATTA = "zenyatta"
        ASHE = "ashe"
        BASTION = "bastion"
        DOOMFIST = "doomfist"
        GENJI = "genji"
        HANZO = "hanzo"
        JUNKRAT = "junkrat"
        MCCREE = "mccree"
        MEI = "mei"
        PHARAH = "pharah"
        REAPER = "reaper"
        SOLDIER76 = "soldier76"
        SOMBRA = "sombra"
        SYMMETRA = "symmetra"
        TORBJORN = "torbjorn"
        TRACER = "tracer"
        WIDOWMAKER = "widowmaker"


    class Field:
        NAME = "name"
        CODENAME = "codename"
    F = Field

    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def j_yaml(cls):
        filepath = os.path.join(FILE_DIR, "character.yaml")
        j = YAMLTool.filepath2j(filepath)
        return j

    @classmethod
    def j_list_all(cls):
        return cls.j_yaml()

    @classmethod
    def j2codename(cls, j):
        return j[cls.F.CODENAME]

    @classmethod
    def j_lang2name(cls, j, lang):
        return jdown(j, [cls.F.NAME, lang])

    @classmethod
    def codename_lang2name(cls, codename, lang):
        j = filter2singleton(lambda j:cls.j2codename(j)==codename, cls.j_list_all())
        name = cls.j_lang2name(j, lang)
        return name
