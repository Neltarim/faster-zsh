from os import getlogin


##### AUTOMATED ########
## DON'T TOUCH IT ######

USR_NAME = getlogin()
DOC_PATH = "/home/{}/Documents".format(USR_NAME)
ZSH_CUSTOM_PATH = "~/.oh-my-zsh/custom/code_aliases.zsh"
GIT_ROOT = "http://github.com/"
PERSONAL_GIT_URL = "{}{}/".format(GIT_ROOT, USR_NAME)
########################


###### MANUAL ##########


DISPLAYS = ["eDP-1", "HDMI-1"] #append the list with the name of your displays
WORKSPACES = [2,1] #append the list if you want to save more workspaces
QWERTY_ON_I3 = True #if you want to setup your keyboard on qwerty with i3
DEFAULT_BRIGHT = "8"

class msql_profile():
    def __init__(self):
        self.host   = "localhost"
        self.usr    = "neltarim"
        self.pwd    = None
        self.db     = None
        self.script = None

########################

###### Neltarim ########

PROP_9_TAP = [305,304,302, 303]
########################