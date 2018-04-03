"""_Summary
#* Default Terminal API:
    Contains various information and functions related to your Inventory.
        FIXME: Review this class before initial release
"""
text = "[zLib]:"

class Inventory:
    @staticmethod
    def GetItemCount(id):
        print(text, "Returns how many of the item id", id, "we have")
        return 1

    @staticmethod
    def GetItemSlotCount(tabid):
        print(text, "Returns max slots you have for tab#", tabid)
        return 100

    @staticmethod
    def GetEmptySlotCount(tabid):
        print(text, "Returns slots left open in tab#", tabid)
        return 50

    @staticmethod
    def FindItemByID(item_id):
        item_id = item_id
        valid = True
        pos = 1, 2
        print(text, "FindItemByID(" + str(item_id) + "): valid =", valid, "| pos =", pos)
        return Item(item_id)            

    @staticmethod
    def GetItems(tab_id):
        print(text, "Returns a list of all items from tab#", tab_id)
        return [1, 2, 3, 4, 5]

    @staticmethod
    def GetItem(tab_id, slot_num):
        print(text, "Returns item from slot", slot_num, " in tab#", tab_id)

    @staticmethod
    def UseItem(item_id):
        print(text, "Uses item with an id of", item_id)

    @staticmethod
    def UseCube(cube_id, slot_num):
        print(text, "Uses a cube with id", cube_id, "on slot number", slot_num, "in your equip tab")

    @staticmethod
    def SendChangeSlotPositionRequest(tab_id, orig_pos, new_pos, count):
        print(text, "Sends a pos change request to tab num", tab_id, " requesting we go from", orig_pos, "to", new_pos, "as new_pos and a stack size of", count)

    @staticmethod
    def UseFamiliarCard(id):
        print(text, "Uses Familiar Card with", id, "as id")

class Item:
    def __init__(self, item_id):  # TODO: Make item class return the same values as it would ingame
        self.option1 = "Inner Pot 1 Placeholder"
        self.option2 = "Inner Pot 2 Placeholder"
        self.option3 = "Inner Pot 3 Placeholder"
        self.grade = "Item Grade Placeholder"
        self.id = item_id
        self.pos = 1, 2
        self.count = 100
        self.valid = True
