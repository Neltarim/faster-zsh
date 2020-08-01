from tools.const import bcolors
from getpass import getpass


def color():
    """ Print all availables colors. """
    bc = bcolors()
    bc.colortest()

def prompt(string, type="header", plus=None):

    fprompt = ""

    if plus == "bold":
        fprompt = bcolors.BOLD

    elif plus == "underline":
        fprompt = bcolors.UNDERLINE

    else:
        pass


    if type == "header":
        fprompt += bcolors.HEADER + "{Faster-zsh}"

    elif type == "okblue":
        fprompt += bcolors.OKBLUE + "{Faster-zsh}"

    elif type == "okgreen":
        fprompt += bcolors.OKGREEN + "{Faster-zsh}"

    elif type == "warning":
        fprompt += bcolors.WARNING + "{Faster-zsh}WARNING :"

    elif type == "fail":
        fprompt += bcolors.FAIL + "{Faster-zsh}ERROR :"

    else:
        prompt("Basic prompt use case: prompt(string, type=\"header\", plus=None)", type="fail", plus="bold")
        exit()

    fprompt += bcolors.ENDC

    if plus == "input":
        print(fprompt + string, end="")
        ans = input()

        return ans

    elif plus == "password":
        str = fprompt + string
        pwd = getpass(str)

        return pwd

    else:
        print(fprompt + string)



