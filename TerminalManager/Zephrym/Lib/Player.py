"""_Summary
Handles basic Player stuff. Will have custom additions later

"""

import inspect

try:
    import Terminal
    import GameState
    import Character
except ModuleNotFoundError:
    warning = "[zLib]:"
    from Lib.Terminal import Terminal
    from Lib.Character import Character
    from Lib.GameState import GameState

class Player:
    def __init__(self, name, job, level):
        self.name = name
        self.job = job
        self.level = level

    def update(self):
        if GameState.IsInGame():
            self.name = Character.GetName()
            self.job = Character.GetJob()
            self.level = Character.GetLevel()

    def go_to(self, mapid):
        Terminal.Rush(mapid)