from os import system as sc
from os import getcwd

from lib.profile import FZSH_PATH

def new_flask(name_pr):
    pr_path = getcwd()
    pr_path += "/" + name_pr
    sc("mkdir " + name_pr)
    sc("touch {}/config.py {}/.gitignore".format(pr_path, pr_path))

    app_name = input("app name :")
    
    app_path = pr_path + "/{}/".format(app_name)
    sc("mkdir {}".format(app_path))
    sc("touch {}__init__.py".format(app_path))
    dirs = ["static", "templates", "tests"]

    for dr in dirs:
        sc("mkdir " + app_path + dr)

    file_to_copy = FZSH_PATH + "/lib/src/flask_views_tpl.py"
    sc("cp {} {}views.py".format(file_to_copy, app_path))

    with open(pr_path + "/run.py", 'w') as file:
        file.write("""
from {}.views import app
        
if __name__ == "__main__":
    app.run(debug=True)""".format(app_name))