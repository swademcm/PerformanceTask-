import time, os

os.system('cls')
# clear the screen
input('Welcome to Fly The Ship, \nFly your ship and gain coins depending on how high you go. Use these coins to upgrade your ship how you like and fly even higher.\n\nTry and get as high as you can! Press Enter to Get Started.\n')
# tutorial / intro

os.system('cls')
# clear the screen
name = input('What is your name?\n')


def loading(message):
# start of loading animation
    os.system('cls')
    print(f"{message}.")
    time.sleep(0.5)
    os.system('cls')
    print(f"{message}..")
    time.sleep(0.5)
    os.system('cls')
    print(f"{message}...")
    time.sleep(1)
    os.system('cls')
# end of loading animation




def home():
    choice = input('''
What would you like to do?
      
F - Fly Ship
S - Open Shop
Q - Quit
''')
    

    if choice == "F":
        print("Taking Off")
    if choice == "Q":
        os.system('cls')
        print("Thanks For Playing!")
        os.abort()

    
loading("")  
home()
