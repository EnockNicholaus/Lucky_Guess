# password generation tool main program
# contains functions for the startup of the program

import time
import os
import random
import colorama

# defining essential basic functions which are used throughout

cls = lambda: os.system('cls')    # this function clears the console screen


def colors(c):                    # the function contains the list of all the colors used in the program
    if c == 1: print(colorama.Fore.LIGHTGREEN_EX)
    if c == 2: print(colorama.Fore.LIGHTBLUE_EX)
    if c == 3: print(colorama.Fore.LIGHTRED_EX)
    if c == 4: print(colorama.Fore.LIGHTYELLOW_EX)
    if c == 5: print(colorama.Fore.WHITE)


def head():                       # this function marks the heading of the program
    cls()
    colors(1)
    print()
    print("|********************************************************************|")
    print("|*                                                                  *|")
    print("|*   _               _                    ____                      *|")
    print("|*  | |   _   _  ___| | ___   _          / ___|_   _  ___  ___ ___  *|")
    print("|*  | |  | | | |/ __| |/ / | | |   ___  | |  _| | | |/ _ \/ __/ __| *|")
    print("|*  | |__| |_| | (__|   <| |_| |  |___| | |_| | |_| |  __/\__ \__ \ *|")
    print("|*  |_____\__,_|\___|_|\_\\__,  |         \____|\__,_|\___||___/___/ *|")
    print("|*                        |___/                                     *|")
    print("|*                                                                  *|")
    print("|*                                                                  *|")
    print("|********************************************************************|")
    print(colorama.Fore.WHITE, "                developer  -  Enock Nicholaus         ")
    print()
    colors(1)
    print("                 ", time.ctime())
    print("\n\n")
    time.sleep(0.5)
    colors(5)
    print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Fore.WHITE, "The Program generates several to thousands of possible victim's\n      Password combinations depending on the victim's details\n")
    time.sleep(0.5)
    print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Fore.WHITE, "The Program is for Education purposes only,\n      I do not take responsibilities for any illegal use")
    time.sleep(0.5)
    

      
def begin():                      # The small heading function
    cls()
    colors(1)
    print(' PASSWORD GENERATION TOOL '.center(70, '*'))
    colors(5)
    time.sleep(0.5)


def error():                      # the function for errors during entering of victim's details(data)
    cls()
    colors(3)
    print(' !! ERROR ERROR ERROR ERROR !! '.center(70, ':'))
    time.sleep(0.5)
    colors(5)


def exiting():                    # the function for exiting the program's console
    cls()
    Exit = 'Exiting..'
    while len(Exit) <= 19:
        colors(2)
        print(Exit)
        Exit += '..'
        time.sleep(0.4)
        cls()
    colors(5)
    print("Goodbye!!")
    time.sleep(1)
    exit()


# The function for Entering the details of the victim
# All the variables must be in string (str) format to avoid errors on data entry

def details():                        
    print("[*] Fill in the following Details,\n    If you do not know the Detail just skip by Pressing Enter key and continue")
    time.sleep(0.5)
    colors(1)
          
    # The variables are in alphabetical order with each alphabet representing a certain kinds of details
    #.
    # The variables are also acompanied with a numerical number
    #.
    # The variable "a" inputs are of the common name and nicknames of the victim
          
    a1 = str(input("ENTER VICTIM'S FIRST NAME:  "))
    a2 = str(input("ENTER VICTIM'S MIDDLE NAME:  "))
    a3 = str(input("ENTER VICTIM'S SURNAME:  "))
    a4 = str(input("ENTER VICTIM'S NICKNAME:  "))
    a5 = str(input("ENTER VICTIM'S OTHER NICKNAME:  ")) 
    colors(5)
    print("[*] Phase 1 Complete!!")
    time.sleep(1)
    begin()

    # The variable "b" inputs are the numerical details of the victim
    # They inlude birthday and mobile number of the victim
    
    print("[*] Enter the following Details in numeral form")
    colors(1)
    b1 = str(input("ENTER VICTIM'S BIRTH YEAR: "))
    b2 = str(input("ENTER VICTIM'S BIRTH MONTH: "))
    b3 = str(input("ENTER VICTIM'S BIRTH DAY: "))
    b4 = str(input("ENTER VICTIM'S MOBILE Number#: "))
    colors(5)
    print("[*] Phase 2 Complete!!")
    time.sleep(1)
    begin()

    # The variable "c" inputs includes the random details about the victims likes
    # They play a major role in the password making
    
    print("[*] Enter the following \"Likes\" Details about the Victim accordingly")
    time.sleep(0.3)
    colors(1)
    c1 = str(input("ENTER VICTIM'S GIRLFRIEND/BOYFRIEND SINGLE NAME: "))
    c2 = str(input("ENTER VICTIM'S GIRLFRIEND/BOYFRIEND NUMBER#: "))
    c3 = str(input("ENTER VICTIM'S FAVOURITE SINGER SINGLE NAME: "))
    c4 = str(input("ENTER VICTIM'S FAVOURITE SONG: "))
    c5 = str(input("ENTER VICTIM'S FAVOURITE TEAM: "))
    c6 = str(input("ENTER VICTIM'S FAVOURITE PLAYER'S SINGLE NAME: "))
    c7 = str(input("ENTER VICTIM'S FAVOURITE ACTER/ACTRESS SINGLE NAME: "))
    c8 = str(input("ENTER VICTIM'S FAVOURITE MOVIE: "))
    colors(5)
    print("[*] Phase 3 Complete!!")
    time.sleep(1)
    begin()

    # the following details are about the passwords characteristics depending on what the user knows where it's applied
    # the variable "e" modify the passwords characteristics to a single type of a match
    # the modules to be called after data entry is complete depend on this "e" variables
    
    print("[*] The following details takes effect on the Password's characteristics")
    colors(1)
    try:
        e1 = eval(input("How long should the password be (e.g 10): "))
    except:
        error()
        print("Wrong data Entry you should enter only numerals")
        time.sleep(1)
        colors(2)
        input("[*] Press Enter to Continue ......")
        begin()
        e1 = eval(input("How long should the password be (e.g 10): "))
    colors(5)
    print("[*] Password should contain?")
    colors(1)
    print("1. alphabets only\n2. Numbers only\n3. alpha_numerical only\n4. All combined")
    colors(5)
    try:
        e2 = eval(input("Enter your choice: "))
    except:
        error()
        print("Wrong data entry!!")
        time.sleep(1)
        colors(2)
        input("[*] Press Enter to Continue ......")
        begin()
        e2 = eval(input("Enter your choice: "))
    colors(1)
    e3 = str(input("Enter the name of the file to save the passwords: "))
    e3 += '.txt'            # Adding the '.txt' extension at the end so as the passwords to be saved in a text file

    # the modules for generating the passwords are called at the bellow conditions
    # the modules are arranged in according to the kind of the passwords to be generated
    
    if e2 == 1:             # the condition calls the module which generates alphabetical passwords only
        pass
    if e2 == 2:             # the condition calls the moduke which generates numerical passwords only
        pass
    if e2 == 3:             # the condition calls the module which generates alphaNumerical passwords only
        pass
    if e2 == 4:             # the condition calls the module which gerates all types of passwords 
        pass


colorama.init()
while True:
    head()
    colors(1)
    input("\n\n [*] Press Enter to Proceed ......")
    begin()
    details()
