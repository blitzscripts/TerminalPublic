"""_Summary
#* Default Terminal API:
    Contains various information and functions for your character.
"""

text = "[zLib]:"

class Character:
    @staticmethod
    def GetID():
        print(text, "Returns Character ID")
        return 12345678

    @staticmethod
    def GetName():
        print(text, "Returns Character Name")
        return "CharacterName"

    @staticmethod
    def GetGender():
        print(text, "Returns Character Gender ID")
        return 0

    @staticmethod
    def GetSkin():
        print(text, "Returns Character Skin ID")
        return 12

    @staticmethod
    def GetFace():
        print(text, "Returns Character Face ID")
        return 23166

    @staticmethod
    def GetHair():
        print(text, "Returns Character Hair ID")
        return 35834

    @staticmethod
    def GetLevel():
        print(text, "Returns Character Level")
        return 250

    @staticmethod
    def GetJob():
        print(text, "Returns Character Job ID")
        return 4212

    @staticmethod
    def GetStr():
        print(text, "Returns Character Str")
        return 5

    @staticmethod
    def GetDex():
        print(text, "Returns Character Dex")
        return 5

    @staticmethod
    def GetInt():
        print(text, "Returns Character Int")
        return 5

    @staticmethod
    def GetLuk():
        print(text, "Returns Character Luk")
        return 5

    @staticmethod
    def GetHP():
        print(text, "Returns current Character HP")
        return 100

    @staticmethod
    def GetMaxHP():
        print(text, "Returns Character Max HP")
        return 150

    @staticmethod
    def GetMP():
        print(text, "Returns current Character MP")
        return 100

    @staticmethod
    def GetMaxMP():
        print(text, "Returns Character Max MP")
        return 150

    @staticmethod
    def GetAP():
        print(text, "Returns Character available AP")
        return 0

    @staticmethod
    def GetSP():
        print(text, "Returns Character available SP")
        return 0

    @staticmethod
    def GetExp():
        print(text, "Returns current Character EXP")
        return 0

    @staticmethod
    def GetPopularity():
        print(text, "Returns Character Fame")
        return 0

    @staticmethod
    def GetMeso():
        print(text, "Returns Character Mesos")
        return 0

    @staticmethod
    def GetWeaponID():
        print(text, "Returns current equipped Character Weapon ID")
        return 1552000

    @staticmethod
    def GetEquippedItemIDBySlot(slot):
        print(text, "Returns current equipped Character Equip ID at slot #" + str(slot))
        return 1000064

    class GetPos():
        x = 123
        y = 456

    @staticmethod
    def GetAlertRemain():
        print(text, "Get Alert Remain")
        return 0

    @staticmethod
    def GetMoveAction():
        print(text, "Returns Move Action")
        return 4

    @staticmethod
    def BasicAttack():
        print(text, "Character Sends Attack Command")

    @staticmethod
    def LootItem():
        print(text, "Character Sends Loot Command")

    @staticmethod
    def TalkToNpc(id):
        print(text, "Character Talks to Npc :" + str(id))

    @staticmethod
    def EnterPortal():
        print(text, "Character Sends Enter Portal Command.")

    @staticmethod
    def Teleport(x, y):
        print(text, "Character will Teleport to the location", str(x) + ",", str(y))

    @staticmethod
    def MoveX(x, timeout):
        print(text, "Character will move to x coord", str(x), "with a timeout of", str(timeout))

    @staticmethod
    def MoveY(y, timeout):
        print(text, "Character will move to y coord", str(y), "with a timeout of", str(timeout))

    @staticmethod
    def AMoveX(x):
        print(text, "Character will move to x coord", str(x))

    @staticmethod
    def AMoveY(y):
        print(text, "Character will move to y coord", str(y))

    @staticmethod
    def StopMove():
        print(text, "Character stops moving")

    @staticmethod
    def Jump():
        print(text, "Character sends the Jump Command")

    @staticmethod
    def JumpDown():
        print(text, "Character sends the Jump Down Command")

    @staticmethod
    def IsOwnFamiliar(id):
        print(text, "Returns if we own a familiar with the id of", str(id))
        return True

    @staticmethod
    # FIXME: This is probably setup wrong. Will fix later when I get the chance.
    class GetBuffs():
        def __init__(self):
            self.valid = True
            self.type = 1
            self.id = 12345

    @staticmethod
    def HasBuff(type, id):
        print(text, "Returns if you have a buff with type", str(type), "(1 for item, 2 for skill) with an id of",
              str(id))
        return True
