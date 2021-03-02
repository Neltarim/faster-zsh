from os import system as sc
from os import getcwd, path, chdir, listdir, mkdir
from os.path import isdir, exists

from lib.profile import GIT_ROOT, PERSONAL_GIT_URL, USR_NAME
from lib.zsh_c import delete_pycache
from tools.termup import prompt


def gitdel():
    """Delete the git repository attached to the active working directory"""
    pr_path = getcwd()
    pr_name = path.basename(pr_path)
    sc("sudo rm -rf .git && hub delete {}".format(pr_name))

def gitignore(auto=False):
    """Create a .gitignore file to the current directory."""
    path = getcwd()
    prompt("name the directory you want to avoid (ex: env/).")
    prompt("When you're done, just press \"ENTER\" to pass ...")

    if exists(path + "/.gitignore"):
        prompt("Gitignore file already exist.")
        exit()

    else:
        dirs = []
        files = []

        loop = True
        while loop == True:
            elem = input("Directoy :")
            if elem == "":
                loop = False

            else:
                dirs.append(elem)

        prompt("Now name the files you want to avoid (ex: text.py)...")
        prompt("When you're done, just press \"ENTER\" to pass ...")
        loop = True
        while loop == True:
            elem = input("File :")
            if elem == "":
                loop = False

            else:
                files.append(elem)

        with open(path + "/.gitignore", "w") as file:
            for name in dirs:
                file.write(name)

            for name in files:
                file.write(name)

    prompt("gitignore file created successfuly.")

def chnpr(old, new):
    """Change the name of the project"""
    path = getcwd()
    old_path = path + "/" + old
    new_path = path + "/" + new

    chdir(old_path)
    gitdel()

    chdir(path)
    sc("mv {} {}".format(old_path, new_path))
    chdir(new_path)
    sc("hub init && hub create")
    gitPush("fresh name !")

    if exists(new_path + "/.gitignore"):
        pass
        
    else:
        gitignore(auto=True)


def rmpr(pr_name):
    """Delete all the project and repository git attached"""
    yn = input("Are you sure to delete {}?(yes/N) :".format(pr_name))
    yn.lower()

    if yn == "yes" or yn == "y":
        sc("hub delete {}".format(pr_name))
        sc("rm -rf ./{}".format(pr_name))


def gitPush(com=None):
    """Push all the files to git with"""

    delete_pycache()
    
    if com == None:
        com = input("Commit :")

    formatted = "\"" + com + "\""

    sc("git add *")
    sc("git commit -m {}".format(formatted))
    sc("git push")


def gitimport(owner, repo_name):
    """Import a personal repository with is name (no url)"""
    repo_path = GIT_ROOT + "{}/{}.git".format(owner, repo_name)

    sc("git clone {}".format(repo_path))


def gitreload(repo_name):
    """Import a personal repository with is name (no url)"""
    repo_path = PERSONAL_GIT_URL + "{}.git".format(repo_name)

    sc("git clone {}".format(repo_path))


def hardpush():
    prompt("THIS FUNCTION IS SILLY. DON'T USE IT.", type="warning", plus="bold")
    a = input('Do it anyway? (y/any key):')
    if a != 'y' or a != 'yes':
        return False
    DOC_PATH = "/home/{}/Documents".format(USR_NAME)
    chdir(DOC_PATH)
    dirs = listdir(DOC_PATH)

    DOC_PATH += "/"

    for project in dirs:
        project_path = DOC_PATH + project
        if isdir(project_path):
            project_l = listdir(project_path)

            for doc in project_l:
                if doc == ".git":
                    chdir(project_path)
                    gitPush(com="[auto save]")


def fgitinit():
    """ Only use if git won't push with gitpush (not working yet ...)"""

    repo_name = path.basename(getcwd())
    prompt("basename: " + repo_name)

    prompt("hub create ...")
    sc("hub init && hub create " + repo_name)
    chdir("../")

    prompt("creating tmp directory ...")
    mkdir("tmp")
    prompt("copying files in tmp directory ...")
    sc("cp -r {}/* ./tmp && sudo rm -rf {}".format(repo_name, repo_name))

    prompt("git reloading ...")
    gitreload(repo_name)

    prompt("copying files into new dir ...")
    sc("cp -r ./tmp/* " + repo_name)
    sc('rm -rf ./tmp')
    chdir("./" + repo_name)

    prompt("Push ...")
    gitPush()
