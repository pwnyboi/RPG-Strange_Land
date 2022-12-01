import os
import time
from test import *

hp = 0
magic = 0
ranged = 0
melee = 0
defence = 0

stats = f"HP: ",hp,"Magic: ",magic,"Ranged: ",ranged,"Melee: ",melee,"Defence: ",defence
menu1 = "1. Check stats \n2. Mine some ore \n3. Exit"
def main_menu():
    print()
    print(menu1)
    main_menu_option = input("Choose an action: ")
    os.system('cls')
    if main_menu_option == "1":
        check_stats()
        main_menu_option = ""
    if main_menu_option == "3":
        exit()

def check_stats():
    os.system('cls')
    print(stats)
    time.sleep(1)
    print('returning to main menu in \n5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    os.system('cls')
    

while True:
    test()
    main_menu()
