# For Premium terminal users. By Zephrym
# DEVELOPMENT FLAG : This may be broken if you try to run it

# Run this script to enable the first 3 inner potentials.

# Local Var Keywords
# c = condition
# d = delay
# m = map
# n = npc
# q = quest
# s = state of the quest
#     0 = dont have in log
#     1 = have in log
#     2 = done or ready to be turned in

from time import sleep

from Character import *
from Quest import *
from GameState import IsInGame

gDelay = 1
level = GetLevel()

def innerPot1():
    #data taken from https://www.gamekiller.net/threads/auto-inner-quests.3260592/
    q = 12394
    s = GetQuestState(q)
    n = 9010000
    c = s != 2 and IsInGame()
    if c:
        StartQuest(q,n)
        sleep(gDelay)

def innerPot2():
    #data taken from https://www.gamekiller.net/threads/auto-inner-quests.3260592/
    q = 12395
    s = GetQuestState(q)
    n = 9010000
    c = s != 2 and IsInGame()
    if c:
        StartQuest(q,n)
        sleep(gDelay)

def innerPot3():
    #data taken from https://www.gamekiller.net/threads/auto-inner-quests.3260592/
    q = 12396
    s = GetQuestState(q)
    n = 9010000
    c = s != 2 and IsInGame()
    if c:
        StartQuest(q,n)
        sleep(gDelay)

if level > 29:
    innerPot1()

if level > 59:
    innerPot2()

if level > 69:
    innerPot3()