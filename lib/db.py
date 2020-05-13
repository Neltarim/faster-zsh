from os import system as sc
from getpass import getpass
import mysql.connector

from lib.profile import USR_NAME
from lib.zsh_c import prompt


def msqlconnect():

    host = "localhost"
    usr = input("user :")
    pwd = getpass("password :")

    charset="--default-character-set=utf8"

    sc("mysql --host={} --user={} --password={} {}".format(host, usr, pwd, charset))



##################################################
#   The following content is not really userfull #
#   so not actually in development for now.      #
##################################################

class msqlcontrol():

    def __init__(self, other=False):
        self.cmd = None
        
        self.alldb = []
        if other == True:
            self.host = input("host adress :")
            self.admn = input("user :")

        else:
            self.host = "localhost"
            self.admn = USR_NAME
        self.pwd = getpass("password :")
        self.db_name = None

        self.db = mysql.connector.connect(
        host=self.host,
        user=self.admn,
        passwd=self.pwd
        )
        self.cursor = None

    def savedb(self):

        mycursor = self.db.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            self.alldb.append(x)

    def showalldb(self):
        for x in self.alldb:
            print(x)

    def connectdb(self):
        
        self.showalldb()

        self.db_name = input("What DB should we open? :")

        self.db = mysql.connector.connect(
            host = self.host,
            user = self.admn,
            passwd = self.pwd,
            database = self.db_name
        )

        self.cursor = self.db.cursor()

    def showtables(self):
        mycursor = self.db.cusor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)

    def createtables(self):

        new_var = None
        name_table = input("Table name :")
        vars = []
        vars_type = []
        formatted_str = name_table

        prompt("NOTE : \"!end\" to stop adding vars to {}".format(name_table))
        
        while new_var != "!end":
            new_var = input("new var name:")
            vars.append(new_var)

        prompt("Assign a type for your variables (ex: VARCHAR(255) ) :")

        for var in vars:
            var_type = input("{} type :".format(var))
            vars_type.append(var_type)

            ############################################################################# it's garbage

        self.cursor.execute("CREATE TABLE {}")

    def newcmd(self):
        
        print("{}".format(self.db_name.upper()))
        self.cmd = input(">")