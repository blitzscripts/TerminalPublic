"""_Summary
#* Main initializer for Zephrym's Lib
TODO: Finish Converting heavily imperative methods to a more functional style to avoid staircases and pyramids of doom.
"""
import time, gc

version = 1.04
text = "[zLib](" + str(version) + "):"
print(text, "is initializing.")
s = time.time()
import fnmatch
import os
from Lib.Settings import Settings

try:
    import Character
    import Context
    import DataType
    import Field
    import GameState
    import Inventory
    import Key
    import Npc
    import Packet
    import Quest
    import Terminal
    from Lib.Npc import *
    from Lib.Player import *
except ModuleNotFoundError:
    from Lib.Character import *
    from Lib.Field import *
    from Lib.GameState import *
    from Lib.Inventory import *
    from Lib.Key import *
    from Lib.Npc import *
    from Lib.Player import *
    from Lib.Packet import *
    from Lib.Quest import *
    from Lib.Terminal import Terminal

def dispose(message, wait = 1, printdeleted = False):
    s = time.time()
    print("gc { Waiting", wait, "seconds before starting }")
    time.sleep(wait)
    print("Started...")
    print("Collecting garbage to dispose... please wait")
    gc.set_debug(gc.DEBUG_SAVEALL)
    gc.collect()
    print(gc.get_stats()[2]['collected'], "items should be cleaned up")
    c = time.time()
    x = 0
    print("Collection took", "{0:.4f}".format(c - s - wait), "seconds. Starting disposal in", wait, "second.")
    time.sleep(wait)
    for item in gc.garbage:
        if printdeleted:
            print("Garbage found! Deleting", item)
        del item
        x += 1
    d = time.time()
    print("Deleted", x, "items in", "{0:.4f}".format(d - c - wait), "seconds.")
    print("gc took a total of", "{0:.4f}".format(d - s), "seconds to complete.")
    print("gc took a total of", "{0:.4f}".format(d - s - (wait * 2)), "seconds to calculate.(ignores sleep time)")
    time.sleep(wait)
    exit(text + " gc { " + message + " }")

def count(comment, path):  # Useful for tracking productivity
    """_Summary
    #* Uses OS Walk to look for py files
    #*   count - print out the some line counts based
    #*   walk - Responsible for file searching
    #*   calc - Responsible for looking through files and counting lines. returns amount of logic and comment lines
    """

    def walk(root = '.', pattern = '*'):  # os walk method
        for walk_path, sub_dirs, files in os.walk(root):  # loop through all the things
            for name in files:  # looping through files
                if fnmatch.fnmatch(name, pattern):  # checks to see if we can find our intended targets
                    yield os.path.join(walk_path, name)  # gimme dat generator object and fix my path

    def calc(root = ''):  # init root as empty optional arg
        logic, notes, summary, elements, fixme, todo = 0, 0, 0, 0, 0, 0  # init our return values so we can add to them as we
        for lib in walk(root, '*.py'):
            for line in open(lib, encoding = "utf8").readlines():
                line = line.strip()
                if line:
                    if line.__contains__('##'):
                        notes += 1
                    elif line.startswith('"""_Summary'):
                        summary += 1
                    elif line.startswith('#*'):
                        elements += 1
                    elif line.__contains__("FIXME"):
                        fixme += 1
                    elif line.__contains__("TODO"):
                        todo += 1
                    else:
                        logic += 1

        return logic, notes, summary, elements, fixme, todo

    return print(text, comment, calc(path)[0], "possible instructions with", calc(path)[1], "notes,", calc(path)[2], "summaries with", calc(path)[3], "elements,", calc(path)[4], "pending fixes and", calc(path)[5], "TODO's from", str(path))


gc.enable()
print("Auto garbage collection:", gc.isenabled())
count("Scripts zLib has", os.getcwd())
count("zLib has", os.getcwd() + "\Lib")
print(text, "has initialized after", "{0:.2f}".format(time.time() - s), "seconds.")
