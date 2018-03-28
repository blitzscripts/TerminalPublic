"""_Summary
#* Default Terminal API:
    Contains various information and functions related to your Inventory.
        FIXME: Review this class before initial release

"""

class Inventory:
    @staticmethod
    def GetItemCount(id):
        print("Returns how many of the item id", id, "we have")
        return 1

    @staticmethod
    def FindItemByID(id):  # FIXME: No clue what this returns. Please report
        print("Searched Item with ID " + id + " in inventory")

    @staticmethod
    def SendChangeSlotPositionRequest(type, orig_pos, new_pos, count):
        print("Sends a pos change request with", type, "as type", orig_pos, "as orig_pos", new_pos, "as new_pos", count,"as count")

    @staticmethod
    def UseFamiliarCard(id):
        print("Uses Familiar Card with",id, "as id")
