"""_Summary
#* Default Terminal API:
    Contains various information about quests
        FIXME: Args and printing need to be changed before initial release
        FIXME: Review this class before initial release. If you see this then you are on the pre-release version

"""

warning = "[zLib]:"


def StartQuest(nQuestID, dwNpcTemplateID):
    print(warning, "Starts Quest with ID", nQuestID, "from NPC with ID", dwNpcTemplateID)


def CompleteQuest(nQuestID, dwNpcTemplateID):
    print(warning, "Completes Quest with ID", nQuestID, "from NPC with ID", dwNpcTemplateID)


def GetQuestState(nQuestID):
    print(warning, "Returns QuestState from Quest with ID", nQuestID)
    return 1


def CheckCompleteDemand(nQuestID, dwNpcTemplateID):
    print(warning, "returns wether or not Quest with ID", nQuestID, "from NPC with ID", dwNpcTemplateID)
    return 0
