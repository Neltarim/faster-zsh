from os import system as sc
from os import getcwd
import json

from tools.termup import prompt
from lib.profile import FZSH_PATH

class module():
    def __init__(self, name):
        self.name = name
        self.installed = None
        self.apt = None
        self.pip = None
        self.npm = None

class installer():

    def __init__(self):
        self.loop = True
        self.main()
        
    def main(self):
        prompt("Welcome to the fzsh installer.\n", plus='bold')
        prompt('What module you want to install?')

        mods = self.parser()

        i = 1
        for mod in mods:
            if mod.installed != True:
                print(str(i) + ". " + mod.name)
                print("     |")
                tmp = []
                tmp += mod.apt + mod.pip + mod.npm

                

                for el in tmp:
                    print("     |__" + el)

                print()

        self.get_module(mods[0]) #let the user pick the mod


        
    def parser(self):
        mods_path = FZSH_PATH + '/lib/src/modules.json'


        with open(mods_path, 'r') as file:
            mods_json = json.load(file)

        modules_formatted = []

        for mod in mods_json:
            tmp = module(mod)
            tmp.installed = mods_json[mod]['installed']

            tmp.apt = mods_json[mod]['apt']
            tmp.pip = mods_json[mod]['pip']
            tmp.npm = mods_json[mod]['npm']

            modules_formatted.append(tmp)

        return modules_formatted

    def get_module(self, mod):

        mods_path = FZSH_PATH + '/lib/src/modules.json'
        
        with open(mods_path, 'r') as file:
            mods = json.load(file)

        #download the mod
        
        mods[mod.name]['installed'] = "True"

        print(mods[mod.name])
        with open(mods_path, 'w') as file:
            json.dump(mods, file, indent=4, separators=(',', ': '))