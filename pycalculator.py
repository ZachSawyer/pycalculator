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
            num1 = int(input("Type the first number to add.\n"))
            screen_clear()
        except ValueError:
            screen_clear()
            print("Please enter a valid number.")
            print("Press enter to contine...")
            input()
            screen_clear()
            continue
        try:
            num2 = int(input("Type a second number to add.\n"))
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
question_loop()
input()




