from sys import argv

from tools.termup import prompt, color
from lib import db
from lib import ithree
from lib import git_c
from lib import zsh_c


FUNC = {
    "noArg" : {
        "msqlscript":   db.msqlScript,
        "gitpush"   :   git_c.gitPush,
        "gitdel"    :   git_c.gitdel,
        "hardpush"  :   git_c.hardpush,
        "aliassave" :   zsh_c.aliassave,
        "xin"       :   zsh_c.forceTapping,
        "wload"     :   ithree.workspace_loader,
        "color"     :   color,
        "aliasup"   :   zsh_c.aliasup,
        "apt"       :   zsh_c.apt,
        "profile"   :   zsh_c.profile_edit,
        "bastion"   :   ithree.bastion,
        "scout"     :   ithree.scout,
        "msqlreset" :   db.kill_process_list,
    },

    "oneArg" : {
        "rmpr"      :   git_c.rmpr,
        "gitreload" :   git_c.gitreload,
        "bright"    :   ithree.bright,
        "quicksql"  :   db.quick_sql_query,
        "wmove"     :   ithree.wmove,
        
    },
    "twoArg" : {
        "chnpr"     :   git_c.chnpr,
        "gitimport" :   git_c.gitimport,
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
