"""_Summary
#* Default Terminal API:
    Contains various information about your Games State.
        FIXME: Review this class before initial release

"""

class GameState:
    @staticmethod
    def GetWorldID():
        print("Returns current world ID")
        return 1

    @staticmethod
    def GetChannel():
        print("Returns current Channel")
        return 1

    @staticmethod
    def IsInGame():  #Python accepts 1/0 as equal to True/False so these return values should be fine
        print("Returns if you are in-game")
        return 1

    @staticmethod
    def IsInCashShop():  
        print("Returns if you are in the cash shop")
        return 1