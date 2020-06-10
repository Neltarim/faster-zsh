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

def quick_sql_query(query):

    msql_params = msql_profile()

    conn = mysql.connector.connect(
            host=msql_params.host,
            user=msql_params.usr,
            password=msql_params.pwd,
            database=msql_params.db
        )
    cursor = conn.cursor()
    cursor.execute(query)
    conn.close()

def execute_query(query, fetch=False, commit=False, payload=None, no_except=False, no_db=False, msg=None):

    msql_params = msql_profile()

    conn = mysql.connector.connect(
            host=msql_params.host,
            user=msql_params.usr,
            password=msql_params.pwd,
            database=msql_params.db
        )
    cursor = conn.cursor()

    try:
        if payload == None:
            cursor.execute(query)

        else:
            cursor.execute(query, payload)

    except:

        if no_except:
            print("WARNING: Exception cancelled.")
            pass

        else:
            print("ERROR: while executing this query :\n" + query)
            yn = input("\nType \"quit\" to leave or press ENTER to continue ...")

            if yn == "quit":
                quit(0)

            else:
                pass

    if fetch:
        rows = cursor.fetchall()
        conn.close()
        return rows
        
    if commit:
        conn.commit()
        
    conn.close()

def kill_process_list():

    process_lst = execute_query("SHOW PROCESSLIST;", fetch=True)

    params = msql_profile()

    i = 0
    for process in process_lst:
        
        if process[7] != "SHOW PROCESSLIST":
            i += 1
            print("{}:{}".format(process[7], process[0]))
            sc("mysqladmin -u {} -p{} kill {}".format(params.usr, params.pwd, process[0]))

    print("{} process killed.".format(i))