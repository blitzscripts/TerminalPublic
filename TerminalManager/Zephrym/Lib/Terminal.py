"""_Summary
#* Default Terminal API:
    Contains various information and functions for Terminal.
        FIXME: Review this class before initial release
        FIXME: Review this class before initial release. If you see this then you are on the pre-release version
"""

text = "[zLib]:"

class Terminal:

    @staticmethod
    def IsRushing():
        print(text, "Returns whether or not Terminal is Rushing somewhere")
        return False

    @staticmethod
    def Rush(id):
        print(text, "Rushes to Map with an ID of ", str(id))

    @staticmethod
    def SetRushByLevel(toggle):
        print(text, "SetRushByLevel has been set to", str(toggle))

    @staticmethod
    def GetFollowID():
        print(text, "Returns current followID")
        return 100

    @staticmethod
    def SetFollowID(id):
        print(text, "Sets the follow id to ", id)

    @staticmethod
    def LoadProfile(path):
        print(text, "Terminal.LoadProfile(" + path + ")")

    @staticmethod
    def SaveProfile():
        print(text, "Saves your current profile")

    @staticmethod
    def Logout():
        print(text, "Logs your character out")

    @staticmethod
    def SetLineEdit(hack, string):
        print(text, "Sets", hack, "to be", str(string))

    @staticmethod
    def SetSpinBox(hack, int):
        print(text, "Sets", hack, "to be", str(int))

    @staticmethod
    def SetSlider(hack, int):
        print(text, "Sets", hack, "to be", str(int))

    @staticmethod
    def SetComboBox(hack, integer):
        print(text, "Sets", hack, "to be", str(integer))

    @staticmethod
    def SetRadioButton(hack, boolean):
        print(text, "Sets", hack, "to be", str(boolean) + ".")

    @staticmethod
    def SetCheckBox(hack, boolean):
        print(text, "Sets", hack, "to be", str(boolean) + ".")

    @staticmethod
    def GetLoginChanel():
        print(text, "Returns your current channel.")
        return 14

    @staticmethod
    def AutoCube(cubeid, slot, grade):
        print(text, "uses a cube with an id of", cubeid, "on the slot", slot, "without a grade of", grade, "1-4")
