# For Premium terminal users. By Zephrym
# Sets your NPC Chat / Harvest keybind to be both space and y simultaneously

from Key import Set

keysToSet = [
    # List of VK's https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
    0x20, # Spacebar
    0x59  # Y
    ]

def setAutoChat(VK):
    Set(VK, 5, 54)

for key in keysToSet:
    setAutoChat(key)