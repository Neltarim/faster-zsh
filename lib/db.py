from os import system as sc
from getpass import getpass
import mysql.connector

from lib.profile import USR_NAME, msql_profile
from lib.zsh_c import prompt
  

def msqlScript():

    default = prompt("Use default mysql profile ? (y/N) :", plus="input")
    db_exist = prompt("Database already exist ? (y/N) :", plus="input")

    prof = msql_profile()

    if default.lower() != "y":
        prof.host = prompt("Host adress :", plus="input")
        prof.usr  = prompt("User :", plus="input")
        
    prof.pwd = prompt("Password :", plus="password")
    prof.script = prompt("Script to use :", plus="input")
    prof.db = prompt("Database name :", plus="input")

    if db_exist.lower() == "y":
        pass

    else:
        conn = mysql.connector.connect(
            host=prof.host,
            user=prof.usr,
            password=prof.pwd
        )
        cursor = conn.cursor()
        query = "CREATE DATABASE {};".format(prof.db)
        cursor.execute(query)
        conn.close()
        
    sc("sudo mysql -h {} -u root -p{} {} < {}".format(prof.host, prof.pwd, prof.db, prof.script))


def msqlconnect():

    host = "localhost"
    usr = input("user :")
    pwd = getpass("password :")

    charset="--default-character-set=utf8"

    sc("mysql --host={} --user={} --password={} {}".format(host, usr, pwd, charset))
