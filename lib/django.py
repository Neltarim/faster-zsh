import subprocess

from os import system as sc
from os import getcwd, chdir, listdir, walk, mkdir, path
from os.path import isdir
from secrets import token_urlsafe

from tools.termup import prompt

def djmanager():
    manager = dj_manager()


class dj_manager():
    """Not finished"""
    def __init__(self):
        self.pr_path = getcwd()
        self.pr_name = path.basename(self.pr_path)
        self.app_name = None

        self.events = {
            'help'      : {
                'desc'  : 'List all functions available',
                'call'  : self.list_events
            },
            'migrate'   : {
                'desc'  : 'Make django migrations and migrate.',
                'call'  : self.migrate
            },
            'mktpl'     : {
                'desc'  : 'Create new templates dir for an app.',
                'call'  : self.djtmpl
            },
            'tree'      : {
                'desc'  : 'Display dir tree.',
                'call'  : self.tree
            },
            'vs'        : {
                'desc'  : 'Open VS Code.',
                'call'  : self.vscode
            },
        }

        self.check_integrity()
        self.list_events([])
        self.event_loop()

    def event_loop(self):
        arg = input('>')
        try:
            args = arg.split()

            self.events[args[0]]['call'](args)
            self.event_loop()
        except:
            prompt('Wrong argument. Please try again.', type='fail')
            self.event_loop()


    def check_integrity(self):
        ok = False
        prompt('Hi. Welcome to the Fzsh django manager.')

        for file in listdir(getcwd()):
            if file == 'manage.py':
                ok = True

        if not ok:
            prompt('It appear that this directory is not a django project yet.', type='fail')
            print('Do you want to create a new project in {} ? (yes/n)\n'.format(self.pr_name))
            inp = prompt('>', plus='input')

            if inp == 'yes' or inp == 'y':
                self.install([])
            else:
                prompt('Exiting.', type="fail")
                exit()

    def rename(self, path):

        for file in listdir(path):
            if isdir(file):
                self.rename(path + '/' + file)

            else:
                tmp_path = path + '/' + file

                with open(tmp_path, 'r') as file :
                    filedata = file.read()

                filedata = filedata.replace('APP_NAME', self.app_name)
                filedata = filedata.replace('PROJECT_NAME', self.pr_name)
                filedata = filedata.replace('SECRET_REPLACE_KEY', token_urlsafe(26))
                filedata = filedata.replace('UPPER_NAME_APP', self.app_name.capitalize())

                with open(tmp_path, 'w') as file:
                    file.write(filedata)


    ############### EVENTS ####################

    def list_events(self, args):
        for i in self.events:
            spaces = 14 - len(i)
            print(i + ' :' + ' ' * spaces + self.events[i]['desc'])

        print()

    def tree(self, args):
        sc('tree')

    def vscode(self, args):
        sc('code .')

    def serv(self, args):
        print('Not working yet.')
        #https://stackoverflow.com/questions/4322624/how-to-make-django-restart-runserver-on-template-change
        #utiliser Thread

    def install(self, args):
        prompt('Welcome to the django-vue project installer.', type='okblue')
        prompt('Installing template ...', type="okblue")
        sc("git clone http://github.com/Neltarim/dj_vue_template.git " + getcwd())
        sc('mv SETTINGS_DIR ' + self.pr_name + '_settings')
        prompt('Template created.', type='okgreen')
        sc('rm -rf .git')

        prompt('Name your first app:', type='header')
        self.app_name = prompt('>', plus='input')
        prompt('Formatting template ...', type='header')
        self.rename(self.pr_path)

        prompt('Creating {} ...'.format(self.app_name), type='header')
        sc('django-admin startapp ' + self.app_name)

        prompt('Creating templates for {} ...'.format(self.app_name), type='header')
        self.djtmpl(auto=True)

        sc('hub init && hub create')
        self.migrate([])


        prompt('Project {} installed successfuly.\n'.format(self.pr_name), type='okgreen')

    def migrate(self, args):
        prompt('Making migrations ...', type='header')
        sc('python3 ./manage.py makemigrations')
        prompt('Migrating ...', type='header')
        sc('python3 ./manage.py migrate')

    def djtmpl(self, auto=False):
        if not auto:
            prompt('What app need a new static template ?\n')
            app_name = prompt('>', plus='input')
        else:
            app_name = self.app_name

        path = getcwd() + '/' + app_name + '/'

        mkdir(path + 'templates')
        mkdir(path + 'static')

        mkdir(path + 'templates/' + app_name)
        mkdir(path + 'static/' + app_name)
        sc('touch ' + path + 'templates/' + app_name + '/index.html')

        prompt('templates and static\'s dirs created.', type='okgreen')


    ############### EVENTS ####################