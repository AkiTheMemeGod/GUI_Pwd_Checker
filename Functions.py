import pandas as pd
import smtplib as sm
import time as tm
import random as rd
from cryptography.fernet import Fernet as fn
import os
import pyperclip as pp
from plyer import notification
import encrypter as en
import shutil as sh

def account():

    while True:
        if os.path.exists("pg_chk_fls/acc_us.txt"):
            print("\n\n\t\t\t\t\tAn user account detected on this machine : \n\n\n ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username == open("pg_chk_fls/acc_us.txt").read() and password == open("pg_chk_fls/acc_pd.txt").read():
                print("\n\n\t\t\t\t\t\tSuccessful login")
                emails = open("pg_chk_fls/acc_email.txt").read()
                return True, emails, username
            else:
                print('Incorrect')
                return False
        else:
            print("\n\n\t\t\t\t\tSince you are new here create an account to use our services : \n\n\n ")
            with open("pg_chk_fls/acc_us.txt", "w") as f:
                f.write(input("Enter a username: "))

            with open("pg_chk_fls/acc_pd.txt", "w") as f:
                f.write(input("Enter a password: "))

            with open("pg_chk_fls/acc_email.txt", "w") as f:
                f.write(input("Enter a email: "))


def gen_key():
    if os.path.exists('pg_chk_fls/mykey.key'):
        with open('pg_chk_fls/mykey.key', 'rb') as keys:
            key = keys.read()
        return key
    else:
        key = fn.generate_key()
        with open('pg_chk_fls/mykey.key', 'wb') as keys:
            keys.write(key)
        return key


def encrypt(key):
    f = fn(key)

    with open('User Accounts/akash/passwords.txt', 'rb') as passes:
        passes = passes.read()

    enc_pass = f.encrypt(passes)

    with open('pg_chk_fls/enc_passwords.txt', 'wb') as enc_passes:
        enc_passes.write(enc_pass)

    with open('User Accounts/akash/usernames.txt', 'rb') as usernames:
        users = usernames.read()

    enc_user = f.encrypt(users)

    with open('pg_chk_fls/enc_usernames.txt', 'wb') as enc_users:
        enc_users.write(enc_user)

    with open('User Accounts/akash/login_credentials.xlsx', 'rb') as logs:
        log = logs.read()

    enc_log = f.encrypt(log)

    with open('pg_chk_fls/enc_login_credentials.xlsx', 'wb') as enc_logs:
        enc_logs.write(enc_log)

    os.remove("User Accounts/akash/passwords.txt")
    os.remove("User Accounts/akash/usernames.txt")
    os.remove("User Accounts/akash/login_credentials.xlsx")


def decrypt(key):
    f = fn(key)

    with open('pg_chk_fls/enc_passwords.txt', 'rb') as enc_passes:
        passes = enc_passes.read()

    dec_pass = f.decrypt(passes)

    with open('User Accounts/akash/passwords.txt', 'wb') as passes:
        passes.write(dec_pass)

    with open('pg_chk_fls/enc_usernames.txt', 'rb') as enc_users:
        users = enc_users.read()

    dec_users = f.decrypt(users)

    with open('User Accounts/akash/usernames.txt', 'wb') as usernames:
        usernames.write(dec_users)

    with open('pg_chk_fls/enc_login_credentials.xlsx', 'rb') as enc_logs:
        log = enc_logs.read()

    dec_logs = f.decrypt(log)

    with open('User Accounts/akash/login_credentials.xlsx', 'wb') as logs:
        logs.write(dec_logs)

    os.remove("pg_chk_fls/enc_passwords.txt")
    os.remove("pg_chk_fls/enc_usernames.txt")
    os.remove("pg_chk_fls/enc_login_credentials.xlsx")


def gen(length):
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    spec = ['!', '@', '#', '$', '%', '&', '=']
    i = 0
    pwd = ""

    def small_gen():
        x = rd.choice(small)
        return x

    def caps_gen():
        y = rd.choice(caps)
        return y

    def num_gen():
        z = rd.randint(0, 9)
        return str(z)

    def spec_gen():
        s = rd.choice(spec)
        return s

    args = [small_gen, caps_gen, num_gen, spec_gen]

    while i < int(length):
        func = rd.choice(args)
        pwd = f"{pwd}{func()}"
        i += 1

    # print(pwd)

    return pwd


def get_pd():
    with open(f"{path}/passwords.txt", 'r') as file:
        passwords = file.readlines()
    return passwords


def put_pd(pwd):
    with open(f"{path}/passwords.txt", 'w') as file:
        file.writelines(pwd)


def get_usr():
    with open(f"{path}/usernames.txt", 'r') as file:
        usernames = file.readlines()
    return usernames


def put_usr(usrn):
    with open(f"{path}/usernames.txt", 'w') as file:
        file.writelines(usrn)


def get_time():
    with open(f"{path}/timestamp.txt", 'r') as file:
        times = file.readlines()
    return times


def put_time(tim):
    with open(f"{path}/timestamp.txt", 'w') as file:
        file.writelines(tim)


def checker(pwd):
    vuln = []
    spec = ['!', '@', '#', '$', '%', '&', '=']
    cap = 0
    spc = 0
    num = 0
    smll = 0
    while True:
        if len(pwd) >= 16:
            for p in pwd:
                if p.isdigit():
                    num += 1

            for p in pwd:
                if p.islower():
                    smll += 1

            for p in pwd:
                if p.isupper():
                    cap += 1

            for p in pwd:
                if p in spec:
                    spc += 1

            break

        else:
            print("character length is below 16 try again : \n")
            break

    if spc >= 3:
        em4 = "✅"
        vuln.append(True)
    else:
        em4 = "❌"
    if cap >= 3:
        em3 = "✅"
        vuln.append(True)
    else:
        em3 = "❌"
    if smll >= 6:
        em2 = "✅"
        vuln.append(True)
    else:
        em2 = "❌"
    if num >= 4:
        em1 = "✅"
        vuln.append(True)
    else:
        em1 = "❌"

    small = f"{smll} /6 small letters - {em2} \n"
    capital = f"{cap} /3 capital letters - {em3} \n"
    number = f"{num}/4 numbers - {em1} \n"
    special = f"{spc} /3 special characters - {em4} \n"
    pass_list = [small, capital, number, special]
    x = 0
    for i in vuln:
        if i:
            x += 1

    return x, pass_list


def save(pwd, usr):
    path = 'User Accounts/' + whose_session()
    pds = []
    usrn = []
    time = []
    pwd = pwd + '\n'
    usr = usr + '\n'
    en.decrypt_folder(path)
    usrn = get_usr()
    usrn.append(usr)
    put_usr(usrn)
    # en.decrypt_file(path)
    pds = get_pd()
    pds.append(pwd)
    put_pd(pds)
    # en.decrypt_file(path)
    time = get_time()
    time.append(tm.asctime() + '\n')
    put_time(time)
    en.encrypt_folder(path)


def show():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def delete():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    delete = int(input("\nMention the row.no you want to be deleted : "))
    df.drop(delete, inplace=True)
    print(df)
    usrn.remove(usrn[delete])
    pds.remove(pds[delete])
    time.remove(time[delete])
    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def clipboard():
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    select = int(input("\nMention the password you want to copy to clipboard (row.no ) : "))
    pp.copy(pds[select])
    print("\n\t\t\tPassword Successfully Copied into the clipboard ✅ ")
    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def edit():
    usrn = []
    pds = []
    time = []

    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]

    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)
    row = int(input("\nMention the row.no you want to edit : "))

    while True:
        editor = input("\nenter U/P to edit Username/Password : ")
        editor.lower()
        if editor == 'u':
            usrn[row] = input("Enter the new username : ")  # + "\n"
            break
        elif editor == 'p':
            pds[row] = input("Enter the new password : ")  # + "\n"
            break
        else:
            print("wrong selection try again .. ")

    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    print(df)

    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]
    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def clear():
    usrn = []
    pds = []
    time = []

    time = get_time()
    time.clear()
    put_time(time)

    usrn = get_usr()
    usrn.clear()
    put_usr(usrn)

    pds = get_pd()
    pds.clear()
    put_pd(pds)


def saving():
    # path = 'User Accounts/' + whose_session()
    usrn = []
    pds = []
    time = []
    time = get_time()
    # time.append(tm.asctime())

    usrn = get_usr()
    pds = get_pd()

    usrn = [i.strip('\n') for i in usrn]
    pds = [i.strip('\n') for i in pds]
    time = [i.strip('\n') for i in time]
    data = {
        "Date/Time": time,
        "USERNAMES": usrn,
        "PASSWORDS": pds
    }
    df = pd.DataFrame(data)
    df.to_excel(f"{path}/login_credentials.xlsx")

    usrn = [i + "\n" for i in usrn]
    pds = [i + "\n" for i in pds]
    time = [i + "\n" for i in time]

    put_usr(usrn)
    put_pd(pds)
    put_time(time)


def otp_gen():
    otp = ""
    for i in range(0, 6):
        z = str(rd.randint(0, 9))
        otp += z
    return otp


def verify_otp(email):
    '''notif("INITIALIZING GENERAL 2-FACT AUTHENTICATION\n"
          f"A 6 digit OTP has been sent to the email {email} \n")'''
    OTP = otp_gen()
    s = sm.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("akis.pwdchecker@gmail.com", "tjjqhaifdobuluhg")
    s.sendmail('akis.pwdchecker@gmail.com', email, OTP)
    return OTP


def notif(message):
    notification.notify(
        title='Password Checker-v2.0',
        message=message,
        app_icon='assets/image.ico',
        timeout=3
    )


"""def get_todos(filepath="pg_chk_fls/passwords.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def put_todos(tds, filepath="pg_chk_fls/passwords.txt"):
    with open(filepath, 'w') as file:
        file.writelines(tds)
"""


def get_account(filename):
    with open(filename, 'r') as file:
        accounts = file.readlines()
    return accounts


def get_account_string(filename):
    with open(filename, 'r') as file:
        accounts = file.read()
    return accounts
# en.decrypt_folder('pg_chk_fls')


def write_session(session_name):
    with open("assets/session.txt", 'w') as file:
        file.write(session_name)


def whose_session():
    with open("assets/session.txt", 'r') as file:
        session = file.read()
    return session


def create_account(directory):
    parent_path = 'C:/PROJECTS/GUI_Pwd_Checker/User Accounts'
    path = os.path.join(parent_path, directory)
    os.mkdir(path)
    sh.copy('assets/passwords.txt', path)
    sh.copy('assets/usernames.txt', path)
    sh.copy('assets/timestamp.txt', path)


global path
path = 'User Accounts/' + whose_session()
