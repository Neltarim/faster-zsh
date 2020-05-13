from sys import argv

from tools.termup import prompt, color
from lib import db
from lib import git_c
from lib import zsh_c


FUNC = {
    "noArg" : {
        "msql"      :   db.mysql,
        "gitpush"   :   git_c.gitPush,
        "gitdel"    :   git_c.gitdel,
        "hardpush"  :   git_c.hardpush,
        "aliassave" :   zsh_c.aliassave,
        "xin"       :   zsh_c.forceTapping,
        "wload"     :   zsh_c.workspace_loader,
        "color"     :   color,
        "aliasup"   :   zsh_c.aliasup,
        "apt"       :   zsh_c.apt,
        "profile"   :   zsh_c.profile_edit
    },

    "oneArg" : {
        "rmpr"      :   git_c.rmpr,
        "gitreload" :   git_c.gitreload,
        "bright"    :   zsh_c.bright
        
    },
    "twoArg" : {
        "chnpr"     :   git_c.chnpr,
        "gitimport" :   git_c.gitimport
    }
}

if __name__ == "__main__":

    argtype = None

    if len(argv) == 2:
        argtype = "noArg"
        FUNC[argtype][argv[1]]()

    elif len(argv) == 3:
        argtype = "oneArg"
        FUNC[argtype][argv[1]](argv[2])

    elif len(argv) == 4:
        argtype = "twoArg"
        FUNC[argtype][argv[1]](argv[2], argv[3])

    else:
        prompt("mmhh .... you're dumb.", type="warning", plus="bold")
        exit(0)
