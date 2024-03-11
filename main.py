import time, os, base64







flightmultiplier = 1
balance = 0
pricemultiplier = 1
name = ""
durationmultiplier = 1
pricemultiplier2 = 1





os.system('cls')
# clear the screen
input('''
Welcome to Fly The Ship! \n
- Fly your ship and gain coins. 
- Use these coins to upgrade your ship.\n
Try and get as high as you can! 
      
Press Enter to Continue.\n''')
# tutorial / intro

os.system('cls')
# clear the screen
def getname():
    global name
    name = input('What is the name of your ship? (3 Letters Minimum)\n')
    if (len(name) < 3):
        os.system('cls')
        input('You need to have atleast 3 characters in your name.\n\nEnter to continue.')
        os.system('cls')
        getname()
        

getname()


        




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
V - Save Game
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
    elif choice == "v":
        os.system('cls')
        input('coming soon.')
        home()
    
    else:
        input("Please enter one of the options above. Press enter to continue")
        os.system('cls')
        home()


def launch():
    global balance
    active = True
    n = 0
    limit = 1000 * durationmultiplier
    while active == True:
        os.system('cls')
    
        print(f"Score: {n}\n{ship}")
        n += 2 * flightmultiplier

        if n > limit:
            balance += n / 100
            balance = round(balance, 0)
            os.system('cls')
            print(f"Ship Crashed!\n\nScore: {n}\nCoins Earned: {round(n / 100, 0)} \nBalance: {balance}\n\nGoing back to menu in 5 seconds.") 
            time.sleep(5)
            os.system('cls')
            active = False

def shop():
    os.system('cls')
    choice = ""
    global flightmultiplier, balance, pricemultiplier, durationmultiplier, pricemultiplier2

    choice = input(f'''
Please choose something to upgrade.
      
F - Flight Multiplier
Cost: {15 * pricemultiplier}
Value: {pricemultiplier}    

D - Flight Duration
Cost: {15 * pricemultiplier2}
Value: {pricemultiplier2}   

Q - Quit
''')
    if (choice == "f"):
        if (balance >= 15 * pricemultiplier):
            balance -= 15 * pricemultiplier
            pricemultiplier += 1
            flightmultiplier += 1
            os.system('cls')
            input('Successfully Purchased. Enter to continue.')
        else:
            os.system('cls')
            input('Balance is not high enough for this purchase. Enter to continue.')
    elif (choice == "q"):
        home()
    elif (choice == "d"):
        if (balance >= 15 * pricemultiplier2):
            balance -= 15 * pricemultiplier2
            pricemultiplier2 += 1
            durationmultiplier += 1
            os.system('cls')
            input('Successfully Purchased. Enter to continue.')
        else:
            os.system('cls')
            input('Balance is not high enough for this purchase. Enter to continue.')

loading("loading")  
home()
