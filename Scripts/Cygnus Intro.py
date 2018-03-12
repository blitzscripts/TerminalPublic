# For Premium terminal users. By Zephrym

# Run this script to clear prequests for new Cygnus characters.
# Will get you right up until right before you select a job

# Standard Python Imports
from time import sleep

# Terminal API Imports
import DataType  # boost::shared_ptr<struct PyTYPE>
from Character import *
from Npc import *
from Field import FindItem, FindMob, GetID
from Inventory import SendChangeSlotPositionRequest, UseItem, GetItemCount
from Key import Press, Set
from Quest import GetQuestState, StartQuest
from Terminal import Rush, SetCheckBox, SetSpinBox

# Config
# gDelay Default Value = 1 (second)
gDelay = 1 # Increase this value if you want the bot to sleep between methods to save some cpu

# Attempts Default Value = 30 (loops)
Attempts = 30 # Number of times the script will re-loop before exiting if something goes wrong.

# Condition's
bNoblesse = GetJob() == 1000 # Job Check
bKill = FindMob(0).valid # Mob Check
bLoot = FindItem(0).valid # Lootable Check

# Nexon likes to re-use NPC Id's so I am storing these in global instead of local
nBird = 1102113
nEmpress = 1102106
nEmpress2 = 1101000
nKia = 1102104
nKimu = 1102101
nKimu2 = 1102114
nKiku = 1102100
nKinu = 1102103
nHawkeye = 1102112
nKizan = 1102102
nNeinheart = 1102107
nNeinheart2 = 1101002

# Function Library
def mapID(m):
    if GetID() == m:
        print("We are currently on the map#" + str(GetID()))
    else:
        print("We are not on " + str(m))
    return GetID() == m

def startQuest(q,n):
    print("Talking to our quest giver with an id#" + str(n))
    TalkToNpc(n)
    sleep(gDelay)
    print("Starting quest#" + str(q) + " from npc#" + str(n))
    StartQuest(q,n)
    sleep(gDelay)

def completeQuest(q,n):
    print("Talking to our quest reciever with an id#" + str(n))
    TalkToNpc(n)
    sleep(gDelay)
    print("Completing quest#" + str(q) + " from npc#" + str(n))
    StartQuest(q,n)
    sleep(gDelay)

def sendKey(VK):
    print("Sending key code " + str(VK))
    Press(VK)

def setKey(VK, nType, nID):
    print("Setting key code" + str(VK) + " with type" + str(nType) + " and ID#" + str(nID))
    Set(VK,nType,nID)

def teleport(x,y):
    print("Teleporting to " + str(x) + ", " + str(y))
    Teleport(x,y)

def talkTo(n):
    print("Attempting to talk to " + str(n))
    TalkToNpc(n)

def goThrough(x,y):
    teleport(x,y)
    print("Sending EnterPortal()")
    EnterPortal()

def needQuest(id):
    print("Quest#" + str(id) + " has a state of " + str(GetQuestState(id)))
    return GetQuestState(id) == 0

def hasQuest(id):
    print("Quest#" + str(id) + " has a state of " + str(GetQuestState(id)))
    return GetQuestState(id) == 1

def doQuest(id):
    print("Quest#" + str(id) + " has a state of " + str(GetQuestState(id)))
    return GetQuestState(id) != 2

def reloadMap(sleepAmount):
    print("Reloading map")
    JumpDown()
    sleep(sleepAmount)

# Setup
if bNoblesse:
    SetCheckBox("Auto NPC", True)
    SetCheckBox("Jump Down Anywhere", True)
    SetCheckBox("Guard God Mode", True)
    SetCheckBox("Full God Mode", False)
    SetCheckBox("30 Sec God Mode", False)

    for x in range(Attempts):
        print("Running attempt #" + str(x + 1))

        # Core
        if mapID(130030000): # Forest of Beginning 1
            startQuest(20820,nKimu)

        if mapID(130030100): # Knight Orientation Area
            q = 20821
            q2 = q + 1

            startQuest(q,nKimu)
            completeQuest(q,nKiku)
            startQuest(q2,nKiku)
            sendKey(0x51) #Q
            sleep(gDelay)
            sendKey(0x1B) #Esc
            completeQuest(q2, nKimu)

        if mapID(130030101): # Forest of Beginnings
            q = 20823
            q2 = q + 1
            q3 = q + 2
            q4 = q + 3
            q5 = q + 4

            if needQuest(q):
                startQuest(q, nKimu)
            if hasQuest(q):
                completeQuest(q, nKimu)
            elif needQuest(q2):
                startQuest(q2, nKimu)
            elif hasQuest(q2):
                print("Equipping our Hat")
                SendChangeSlotPositionRequest(1, 1, -1, -1)
                sleep(gDelay)
                completeQuest(q2, nKimu)
            elif needQuest(q3):
                startQuest(q3, nKinu)
            elif hasQuest(q3):
                completeQuest(q3, nKinu)
            elif needQuest(q4):
                startQuest(q4, nKinu)
            elif hasQuest(q4):
                completeQuest(q4, nHawkeye)
            elif needQuest(q5):
                startQuest(q5, nKimu)
            elif hasQuest(q5):
                goThrough(-991,88)

        if mapID(130030102): # Physical Training Yard
            q = 20827
            q2 = q + 1
            if doQuest(q):
                completeQuest(q, nKimu2)
            if needQuest(q2):
                startQuest(q2, nKimu2)
            if hasQuest(q2):
                teleport(-2539,-173)
                completeQuest(q2, nKimu)

        if mapID(130030103): # Drill Hall
            q = 20829
            q2 = q + 1
            q3 = q + 2
            q4 = q + 3
            q5 = q + 4
            item = 4000489
            mob = 9300730
            bKill = FindMob(mob).valid # Training Tino
            bLoot = FindItem(item).valid # Tutorial Tino's Feather
            if needQuest(q):
                startQuest(q, nKizan)
            elif hasQuest(q): 
                SetCheckBox("Mob Vac", True)             
                while bKill:
                    BasicAttack()
                    sleep(gDelay)
                    bKill = FindMob(mob).valid # Update's bKill so we can exit the loop
                SetCheckBox("Mob Vac", False)
                completeQuest(q,nKizan)
            elif needQuest(q2):
                StartQuest(q2, nKimu)
            elif hasQuest(q2):
                UseItem(2001555) # Use Electrolyte Drink
                completeQuest(q2, nKimu)
            elif needQuest(q3):
                startQuest(q3, nKizan)
            elif hasQuest(q3):
                x = -369
                y = 7
                teleport(x,y)
                SetCheckBox("Mob Vac", True)
                while bKill:
                    bLoot = FindItem(item).valid # Update's bLoot so we can exit the loop
                    if bLoot:
                        teleport(FindItem(item).x, FindItem(item).y)
                        LootItem()
                        sleep(gDelay)
                    else:
                        BasicAttack()
                    sleep(gDelay)
                    bKill = FindMob(mob).valid # Update's bKill so we can exit the loop
                    bLoot = FindItem(item).valid # Update's bLoot so we can exit the loop
                while bLoot:
                    teleport(FindItem(item).x, FindItem(item).y)
                    LootItem()
                    sleep(gDelay)
                    bLoot = FindItem(item).valid # Update's bLoot so we can exit the loop
                completeQuest(q,nKizan)
                SetCheckBox("Mob Vac", False)
            elif needQuest(q4):
                startQuest(q4, nKizan)
            elif hasQuest(q4):
                completeQuest(q4, nKizan)
            elif needQuest(q5):
                startQuest(q5, nBird)

        if mapID(130030104): # The Tranquil Garden
            q = 20833
            q2 = q + 1
            q3 = q + 2
            q4 = q + 3

            if hasQuest(q):
                SetCheckBox("Auto NPC", False) # Auto NPC will bug this next quest out so we #need to reload the map in order to complete it
                reloadMap(5) # increase this if you still get stuck at Cygnus.
                teleport(-477,88) # You need to be near cygnus in order to turn 20833 in
                SetCheckBox("Auto NPC", True) # Auto NPC should take care of the rest now
                completeQuest(q, nBird)
                
            if needQuest(q2):
                startQuest(q2, nEmpress)
            if hasQuest(q2):
                completeQuest(q3, nNeinheart)
            if needQuest(q3):
                startQuest(q3,nNeinheart)
            if hasQuest(q3):
                completeQuest(q3, nHawkeye)
            if needQuest(q4):
                startQuest(q4, nKizan)

        if mapID(130030105): # Drill Hall (Second instance)
            q = 20837
            mob = 9300731

            if needQuest(q):
                startQuest(q, nKizan)
            if hasQuest(q):
                bKill = FindMob(mob).valid # Update's bKill
                setKey(0x41,1,10001244)
                SetCheckBox("Mob Vac", True)
                while bKill:
                    sendKey(0x41) # Kill the Tinos with our bound skill
                    sleep(gDelay)
                    bKill = FindMob(mob).valid # Update's bKill so we can exit the loop
                SetCheckBox("Mob Vac", False)
                completeQuest(q, nKizan)

        if mapID(130030106): # Forest of Beginnings (Box Stage)
                q = 20838
                q2 = q + 1
                item = 4033670
                bLoot = FindItem(item).valid # Proof of Exam

                if needQuest(q):
                    startQuest(q, nKia)
                if hasQuest(q):
                    x = 1875
                    y = -212
                    teleport(x,y)
                    SetCheckBox("Mob Vac", True)
                    while GetItemCount(item) < 3:
                        bLoot = FindItem(item).valid # Proof of Exam
                        if bLoot and GetItemCount(item) < 3:
                            teleport(FindItem(item).x, FindItem(item).y)
                            sleep(gDelay * 2)
                            LootItem()
                            sleep(gDelay * 2)
                            teleport(x,y)
                        else:
                            BasicAttack()
                        sleep(gDelay)
                    if GetItemCount(item) == 3:
                        completeQuest(q, nKia)
                    SetCheckBox("Mob Vac", False)

                if needQuest(q2):
                    startQuest(q2, nKiku)
                if hasQuest(q2):
                    Rush(130000000) # Ereve
        
        if mapID(130000000): # Ereve
            q = 20839
            q2 = 20860
            if hasQuest(q):
                completeQuest(q, nEmpress2)
                
            if needQuest(q2):
                ClearSelection()
                RegisterSelection("(Lv.10) The Five Paths")
                startQuest(q2, nNeinheart2)
            if GetQuestState(q2) == 2:
                teleport(-1160, 88)
                while bNoblesse:
                    print("Please click the NPC for job you would like") # Too lazy to find all these for auto turn in.
                    bNoblesse = GetJob() == 1000 # Update Job Check
                    sleep(gDelay)

        bNoblesse = GetJob() == 1000 # Update Job Check
        if bNoblesse:
            print("Script has exited with unexpected error... Try increasing your attempt amount. If the issue persists then please report this to Zephrym @ https://www.gamekiller.net/conversations/add")
else:
    print("Nothing else to do. Exiting")
