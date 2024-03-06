import time, os
os.system('cls')
input('Welcome to Fly The Ship, \nFly your ship and gain coins depending on how high you go. Use these coins to upgrade your ship how you like and fly even higher.\n\nTry and get as high as you can! Press Enter to Get Started.\n')
os.system('cls')
name = input('What is your name?\n')
os.system('cls')
print(".")

time.sleep(0.5)
os.system('cls')
print("..")
time.sleep(0.5)
os.system('cls')
print("...")
time.sleep(1)

os.system('cls')
print(f'Welcome, {name}\n\n')
input('''
What would you like to do?
      
F - Fly Ship
S - Open Shop
Q - Quit
''')
