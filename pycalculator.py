import os

os.system("cls")

def display_title():
    title = "Calculator"
    padded_text = title.center(200)
    print(padded_text)

def question_loop():
    try:
        print("Please type a number you would like to add.")
        userResponse1 = input()
        print("Thank you. Now type in a second number")
        userResponse2 = input()
        num1 = int(userResponse1)
        num2 = int(userResponse2)
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
        return total
    except ValueError:
        print("Invalid input. Please enter a number.")

display_title()
print("\n")
print("\n")
question_loop()
input()


