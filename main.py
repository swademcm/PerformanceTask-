import time, os

balance = 0



os.system('cls')
# clear the screen
input('''
Welcome to Fly The Ship, \n
Fly your ship and gain coins. Use these coins to upgrade your ship.
Try and get as high as you can! 
      
Press Enter to Get Started.\n''')
# tutorial / intro

os.system('cls')
# clear the screen
name = input('What is your ships name?\n')

ship = f"""
           _
          / \ 
         / _ \ 
        | ( ) |
        |     | 
        | {name[:3]} | 
        |  _  |
        | | | |
        | | | |
        | | | |
       /  | |  \ 
     /    | |    \ 
    /     |_|     \ 
   (_______________)
                                                                                           
"""




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
    choice = ""
    choice = input('''
What would you like to do?
      
F - Fly Ship
S - Open Shop
Q - Quit
''')
    
    if choice == "f":
        loading("launching")
        launch()
        home()
    elif choice == "s":
        shop()
        home()
    elif choice == "q":
        os.system('cls')
        print("Thanks For Playing!")
        os.abort()
    
    else:
        input("Please enter one of the options above. Press enter to continue")
        os.system('cls')
        home()


def launch():
    global balance
    active = True
    n = 0
    limit = 1000
    while active == True:
        os.system('cls')
    
        print(f"Score: {n}\n{ship}")
        n += 2

        if n > limit:
            balance += n / 100
            balance = round(balance, 0)
            os.system('cls')
            print(f"Ship Crashed!\n\nScore: {n}\nCoins Earned: {round(n / 100, 0)} \nBalance: {balance}\n\nGoing back to menu in 5 seconds.") 
            time.sleep(5)
            os.system('cls')
            active = False

def shop():
    print('shop')


loading("loading")  
home()
