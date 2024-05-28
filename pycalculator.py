import os

os.system("cls")

def display_title():
    title = "Calculator"
    padded_text = title.center(250)
    print(padded_text)

def question_loop():
    while True:
        try:
            print("Type the first number to add.")
            num1 = int(input())
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("Please enter a valid number.")
            print("Press any key to contine...")
            input()
            os.system("cls")
            continue
        try:
            print("Type a second number to add.")
            num2 = int(input())
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("Please enter a valid number.")
            print("Press any key to contine...")
            input()
            os.system("cls")
            continue
        print(f'{num1} + {num2} = {num1 + num2}')
        break
        

display_title()
question_loop()
input()




