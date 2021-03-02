from os import system as sc
from os import getcwd, chdir, listdir, walk
from os.path import isdir
import mysql.connector
import logging

from lib.profile import USR_NAME, ZSH_CUSTOM_PATH, PROP_9_TAP, msql_profile, FZSH_PATH
from tools.termup import prompt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOOP = True

def aliasup():
    sc("rm -rf {}".format(ZSH_CUSTOM_PATH))

    chdir("/home/{}/Documents/faster-zsh".format(USR_NAME))
    sc("cp ./code_aliases.zsh {}".format(ZSH_CUSTOM_PATH))
    prompt("New alias saved locally. Please use \"src\" to update your terminal.")

def aliassave():
    aliasup()
    com = input("commit :")

    sc("git add code_aliases.zsh")
    sc("git commit -m \"{}\"".format(com))
    sc("git push origin master")

def forceTapping():
    # WARNING: Function Deprecated. use only "xin" alias.
    for prop in PROP_9_TAP:
        sc("xinput set-prop 10 {} 1".format(prop))

def apt():
    prompt("Welcome to the installer environnement.", type="okblue")

    while LOOP:
        prompt("Name the package you need to install now or quit/ENTER to exit.")
        pkg = input(">")

        if pkg == "" or pkg == "quit":
            prompt("Have a nice coding day.", type="okblue", plus="bold")
            exit()

        else:
            sc("sudo apt-get install {}".format(pkg))

def profile_edit():
    sc("vs ~/Documents/faster-zsh/lib/profile.py")

def kill_port(port):
    sc("sudo fuser -k {}/tcp".format(port))

def pcache_lister(path, pc_lst=[]):
    
    dirs = listdir(path)

    for file in dirs:
        if file == "__pycache__":
            pc_lst.append(path + "/" + file)
            pass

        if isdir(path + "/" + file) == True:
            new_path = path + "/" + file
            pcache_lister(new_path, pc_lst=pc_lst)

    return pc_lst

def delete_pycache():

    root_path = getcwd()
    pc_lst = pcache_lister(root_path)

    for cache in pc_lst:
        sc("sudo rm -rf " + cache)
        prompt("Deleting {} ...".format(cache))
        

    if pc_lst == []:
        prompt("No pycache detected.", type="fail", plus="bold")

    else:
        prompt("All pycaches has been deleted.", type="okgreen")


def parse_files(root, paths=[]):

    for file in listdir(root):

        if file != ".git":
            
            file_path = root + "/" + file
            paths.append(file_path)

            if isdir(file_path):
                parse_files(file_path, paths=paths)

    return paths

def rchmod(mods, dir_name):

    path = getcwd() + "/" + dir_name

    if mods == None:
        prompt("Mods invalid or missing.", type="fail", plus="bold")
        
    paths = parse_files(path)

    for path in paths:
        sc("sudo chmod {} {}".format(mods, path))
        print(path)