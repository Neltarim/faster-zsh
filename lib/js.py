from os import system as sc
from os import getcwd, chdir

def expoNew(name_pr):
    sc("sudo expo init " + name_pr)
    pr_path = getcwd() + "/" + name_pr
    chdir(pr_path)

    sc("sudo n stable && sudo npm install")