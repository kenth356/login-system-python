# Log-in System in Python
# Mariano, Kenth Jarren S.

from dataclasses import dataclass
from typing import List
import sys

usersD: List['userDC'] = []
REGISname = ""

@dataclass
class userDC:
    name: str
    passw: str

def REGIS():
    global usersD
    print("\n\n" + "===============================".rjust(75))
    print("[  REGISTRATION  ]".rjust(68))
    print("===============================".rjust(75))
    print("\n" + "--------------------------------------------------------".rjust(88))
    newUSERS = userDC("", "")
    newUSERS.name = input("\n" + "Enter your full name: ".rjust(54))
    print("\n" + "--------------------------------------------------------".rjust(88))
    newUSERS.passw = input("\n" + "Create your password: ".rjust(54))
    usersD.append(newUSERS)
    SAVEDFILES()
    print("\n" + "--------------------------------------------------------".rjust(88))
    print("\n" + "--------------------------------------------------------".rjust(88))
    print("[  REGISTRATION SUCCESSFUL  ]".rjust(74))
    print("\n" + "--------------------------------------------------------".rjust(88))

def LOGIN():
    global REGISname
    while True:
        LOGINname = ""
        LOGINpass = ""
        USERHANDLING = False
        PASSHANDLING = False
        print("\n\n" + "===============================".rjust(75))
        print("[  LOG - IN  ]".rjust(66))
        print("===============================".rjust(75))
        print("\n" + "--------------------------------------------------------".rjust(88))
        LOGINname = input("\n" + "Enter your full name: ".rjust(54))
        print("\n" + "--------------------------------------------------------".rjust(88))
        LOGINpass = input("\n" + "Enter your password: ".rjust(54))
        print("\n" + "--------------------------------------------------------".rjust(88))
        for users in usersD:
            if users.name == LOGINname:
                USERHANDLING = True
                if users.passw == LOGINpass:
                    PASSHANDLING = True
                    print("\n" + "--------------------------------------------------------".rjust(88))
                    print("\n" + "[  LOG - IN SUCCESSFUL  ]".rjust(72))
                    print("\n" + "--------------------------------------------------------".rjust(88))
                    REGISname = users.name
                    HOMESCR()
                    return
                break
        if not USERHANDLING:
            print("\n" + "--------------------------------------------------------".rjust(88))
            print("\n" + "[  USER NOT FOUND  ]".rjust(70))
            print("\n" + "--------------------------------------------------------".rjust(88))
        elif not PASSHANDLING:
            for i in range(3):
                print("\n" + "--------------------------------------------------------".rjust(88))
                print("\n" + "[  INCORRECT INPUT  ]".rjust(71))
                print("\n" + "--------------------------------------------------------".rjust(88))

def HOMESCR():
    while True:
        print("\n\n" + "============================================".rjust(82))
        print(f"[  WELCOME  {REGISname} ]".rjust(73))
        print("============================================".rjust(82))
        print("\n" + "1. Return".rjust(48))
        print("--------------------------------------------------------".rjust(88))
        try:
            choice = int(input("\n\n" + "Enter: ".rjust(39)))
        except ValueError:
            choice = -1
        if choice == 1:
            return
        else:
            print("\n" + "--------------------------------------------------------".rjust(88))
            print("\n" + "[  PLEASE ENTER A CORRECT INPUT  ]".rjust(76))
            print("\n" + "--------------------------------------------------------".rjust(88))

def EXIT():
    print("\n\n" + "--------------------------------------------------------".rjust(88))
    print("\n" + "[  THANK YOU  ]".rjust(67))
    print("\n" + "--------------------------------------------------------".rjust(88))

def SAVEDFILES():
    with open("users.txt", "w") as file:
        for users in usersD:
            file.write(f"NAME: {users.name}\nPASSWORD: {users.passw}\n")

def main():
    while True:
        print("\n\n" + "================================".rjust(75))
        print("[   WELCOME   ]".rjust(66))
        print("================================".rjust(75))
        print("\n" + "1. Registration           2. Log in          3. Exit".rjust(86))
        print("----------------------------------------------------------".rjust(89))
        try:
            choice = int(input("\n\n" + "Enter: ".rjust(39)))
        except ValueError:
            choice = -1
        if choice == 1:
            REGIS()
        elif choice == 2:
            LOGIN()
        elif choice == 3:
            EXIT()
            return
        else:
            print("\n" + "--------------------------------------------------------".rjust(88))
            print("\n" + "[  PLEASE ENTER A CORRECT INPUT  ]".rjust(76))
            print("\n" + "--------------------------------------------------------".rjust(88))

if __name__ == "__main__":
    main()
