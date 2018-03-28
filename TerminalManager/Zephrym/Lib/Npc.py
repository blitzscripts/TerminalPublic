"""_Summary
Doubles as a Lib.Npc ingame and Npc for IDE due to package loading.
Handles basic NPC stuff. Will have custom additions later
"""

import inspect

try:
    from Npc import *
    from Quest import *
except ModuleNotFoundError:
    warning = "[zLib]:"
    from Lib.Quest import *

    def ClearSelection():
        print(warning, "Clears your selection")

    def RegisterSelection(string):
        print(warning, "Registers", string)

class Npc:
    def __init__(self, npcid, name = None, mapid = None):
        self.id = npcid
        self.name = name
        self.mapid = mapid

    def __register_assert(self, string, s_0_3, s_1_2, s_1_4):
        try:
            assert type(string) is str
            if type(self.name) is str:
                if type(self.mapid) is not None: print("Registering", string, "in prep for", self.name, "on map#", self.mapid)
                else: print("Registering", string, "in prep for", self.name)
            else:
                if type(self.mapid) is not None: print("Registering", string, "in prep for", self.id, "on map#", self.mapid)
                else: print("Registering", string, "in prep for", self.id)
            RegisterSelection(string)
        except AssertionError or NameError:
            print(str(s_0_3) + "() has thrown an error!\n" + "You used", string, "as a",
                  str(type(string)) + " only use string value. \n" + "your implementation of Settings." + str(s_0_3) + "() is incorrect. please inspect it on line (" + str(s_1_2) + ") : You most likely have a syntax error here: " + str(s_1_4))

    def register_selection(self, text):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Npc.__register_assert(self, text, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def clear_selection():
        ClearSelection()

    def start_quest(self, questid):
        StartQuest(questid, self.id)
