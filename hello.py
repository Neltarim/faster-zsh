#/usr/bin/python3.6
# -*-coding:Utf-8 -*
from os import system as sc
import logging

from lib.profile import USR_NAME, QWERTY_ON_I3, DEFAULT_BRIGHT
from lib.zsh_c import forceTapping, workspace_loader, prompt, bright


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello():
    """Start to work's function"""
    bright(DEFAULT_BRIGHT)
    prompt("Hello {}, have a nice coding day.".format(USR_NAME))

    workspace_loader()

    if USR_NAME == "neltarim":
        prompt("Enabling tapping on trackpad.")
        forceTapping()

    if QWERTY_ON_I3 == True:
        prompt("setting keyboard on QWERTY.")
        sc("setxkbmap us")
        
    

if __name__ == "__main__":
    hello()
