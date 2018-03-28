"""_Summary
#* Default Terminal API:
    Contains various information about your Map.
"""

class Field:
    @staticmethod
    def GetID():
        print("Returns current Field ID (Map ID)")
        return 12341234

    @staticmethod
    def FindItem(id):
        print("Searches for Item", id, "in current map")

    @staticmethod
    class FindMob:
        def __init__(self, id):
            self.x = 1
            self.y = 12345

    @staticmethod
    class FindNpc:
        def __init__(self, id):
            self.x = 1
            self.y = 12345

    @staticmethod
    class FindPortal:
        def __init__(self, name):
            self.x = 1
            self.y = 12345

    @staticmethod
    class FindReactor:
        def __init__(self, id):
            self.x = 1
            self.y = 12345

    @staticmethod
    def GetCharacters():  #FIXME: Change this to a class that mimics the datatype so we can return and enable intelli-sense
        print("Returns a vector<DataType.CHARACTER> of current chars in map.")

    @staticmethod
    def FindCharacter(info):  #FIXME: Untested return value. Please report if this is wrong
        print("Returns if we can find a character with", info, "as name or id.")
        return True

    @staticmethod
    def GetCharacterCount():
        print("Returns the character count of the map you are in.")
        return 0
