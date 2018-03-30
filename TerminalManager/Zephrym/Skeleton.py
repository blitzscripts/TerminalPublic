# FIXME: Review this class before initial release. If you see this then you are on the pre-release version
"""_Summary
#*    IDE Enabled Script Skeleton by Zephrym. For Premium Terminal users

#*    Features:
#*      * Intellisense - Context aware auto completion for the entire Terminal API and even some extra features the API does not support natively.
            Scripting more accessible to new users willing to learn and less tedious or time consuming to accomplish complex or meaningful scripts.

#*      * Traceback Error Handling - 90% of errors developers can make will be printed out down to the exact line and code context that was wrong.
             Sometimes wont catch NameError if you reference an undefined variable in the Skeleton.py

#*      * Settings Manager - All of the possible settings that are inside your XML are handled by a custom Settings Class.
             No more need to look through an XML to change a checkbox only to find confusing vague names or abbreviations that make no sense.

#*      * Out of Game Development - Running your scripts inside your IDE or via console instead of through Terminal(GK) will load placeholder classes.
             These classes will print out what the Terminal API should do. Works in 95% of cases please report any issues so they can get fixed.

#*      * Progress Tracking support - When zLib is initialized you will see a print of various information about your working directory that can be used to gauge various goals.
            Remember - More is not always better!
            How to Use
            ## This is a note instead of a comment. Comments are not tracked but notes are. Use this if you need to add a note.(Vague comment)
            " ""_Summary This will track your doc-string as a summary. (remove the space so its 3 consecutive ")
            #* This is a Summary element instead of a comment. Summary elements are contained in summaries and used to define various things.
                only element tag one per description. Use in combo with :param :return
            TODO: This is how you track a TODO inside a summary.
            # TODO: This is how you track a TODO outside a summary. Only use 1 # not 2
            FIXME: TODO rules apply to FIXME

#*   Getting Started:
     1.) Make a copy of your Skeleton.py and rename it as you please.
     2.) Inside your Renamed.py Fill out your script inside the Main Script Logic Region. -- See guide for more details
     3.) You can safely remove this entire doc string to not have clutter at the top of your script.
"""


# region Setup
import os
import sys
if not any("Zephrym" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\Zephrym")
else:
    try: from Lib import *
    except ModuleNotFoundError:
        print("WARNING: [ModuleNotFoundError] has been thrown!")
        print("Something went wrong when attempting to import zLib. Please check your install")
        print("If the issue persists please contact Zephrym for further assistance")
        dispose("ended the program for security reasons due to [ModuleNotFoundError]")
# endregion

# region Main Script Logic
# TODO: Your script goes here. Do not indent
# endregion

# region Garbage Collection
dispose("It looks like our script has nothing else to do. contact the script developer if you think this is a bug")
# endregion
