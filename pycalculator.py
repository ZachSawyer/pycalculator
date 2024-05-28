import os

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    title = "Calculator"
    padded_text = title.center(250)
    print(padded_text)

def question_loop():
    while True:
        try:
            print("Type the first number to add.")
            num1 = int(input())
            screen_clear()
        except ValueError:
            screen_clear()
            print("Please enter a valid number.")
            print("Press enter to contine...")
            input()
            screen_clear()
            continue
        try:
            print("Type a second number to add.")
            num2 = int(input())
            screen_clear()
        except ValueError:
            screen_clear()
            print("Please enter a valid number.")
            print("Press enter to contine...")
            input()
            screen_clear()
            continue
        print(f'{num1} + {num2} = {num1 + num2}')
        break
        
screen_clear()
display_title()
question_loop()
input()




