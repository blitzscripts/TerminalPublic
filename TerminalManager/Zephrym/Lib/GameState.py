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
    def IsInGame():  #FIXME: Untested return value. Please report if this is wrong
        print("Returns if you are in-game")
        return 1
