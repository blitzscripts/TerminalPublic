from Character import *
from Quest import *
#Some sort of inner ability script
#Zephryms cleaned up Inner Pot defs

# Local Var Keywords
# c = condition
# d = delay
# m = map
# n = npc
# q = quest
# s = state of the quest, 0 = dont have in log, 1 = have in log, 2 = done or ready to be turned in


# inner pot taken from https://www.gamekiller.net/threads/auto-inner-quests.3260592/

def innerPot1():
    q = 12394
    s = GetQuestState(q)
    n = 9010000
    c = s != 2
    if c:
        StartQuest(q, n)`

def innerPot2():
    q = 12395
    s = GetQuestState(q)
    n = 9010000
    c = s != 2
    if c:
        StartQuest(q, n)

def innerPot3():
    q = 12396
    s = GetQuestState(q)
    n = 9010000
    c = s != 2
    if c:
        StartQuest(q, n)

def getInnerPot():
    innerPot1()
    innerPot2()
    innerPot3()

if level > 100():
    getInnerPot()
else:
    print("We are not over level 100")

