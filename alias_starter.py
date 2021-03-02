from sys import argv

from tools.termup import prompt, color
from lib import db
from lib import ithree
from lib import git_c
from lib import zsh_c
from lib import py_pr
from lib import js
from lib import downloader
from lib import django


FUNC = [
    {
        "msqlscript"    :   db.msqlScript,
        "gitpush"       :   git_c.gitPush,
        "gitdel"        :   git_c.gitdel,
        "hardpush"      :   git_c.hardpush,
        "aliassave"     :   zsh_c.aliassave,
        "wload"         :   ithree.workspace_loader,
        "color"         :   color,
        "aliasup"       :   zsh_c.aliasup,
        "apt"           :   zsh_c.apt,
        "profile"       :   zsh_c.profile_edit,
        "bastion"       :   ithree.bastion,
        "scout"         :   ithree.scout,
        "msqlreset"     :   db.kill_process_list,
        "delcache"      :   zsh_c.delete_pycache,
        "finstaller"    :   downloader.installer,
        "fgitinit"      :   git_c.fgitinit,
        "herokuconsole" :   py_pr.herokuconsole,
        "djmanager"     :   django.djmanager,
    },

    {
        "rmpr"          :   git_c.rmpr,
        "gitreload"     :   git_c.gitreload,
        "bright"        :   ithree.bright,
        "quicksql"      :   db.quick_sql_query,
        "wmove"         :   ithree.wmove,
        "killport"      :   zsh_c.kill_port,
        "newflask"      :   py_pr.new_flask,
        "exponew"       :   js.expoNew,
        
    },

    {
        "chnpr"         :   git_c.chnpr,
        "gitimport"     :   git_c.gitimport,
        "brightfor"     :   ithree.bright_for,
        "rchmod"        :   zsh_c.rchmod,
    }
]

if __name__ == "__main__":

    func_name = argv[1]
    argtype = len(argv) - 2

    if argtype == 0:
        FUNC[argtype][func_name]()

    elif argtype == 1:
        FUNC[argtype][func_name](argv[2])

    elif argtype == 2:
        FUNC[argtype][func_name](argv[2], argv[3])

    else:
        prompt("mmhh .... you're dumb.", type="warning", plus="bold")
        exit(0)