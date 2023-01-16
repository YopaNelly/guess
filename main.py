print("HELLO what is your name please? ", end= '')
name = input()
print("Hiiy", name.upper(), "you are well come\nHere is a Game for you hope you will enjoy")
print("you have to guess a number from 1 too a number of your choise hope you will WIN)")
x = int(input(f"{name} enter your choise! "))
import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number from 1 to {x}: "))
        if guess < random_number:
            print(f"sorry, guess again. {guess} is Too low. ")
        elif guess > random_number:
            print(f"sorry guess again. {guess} is Too high. ")
    print(f"Yeah, congrats. you guessed the number {random_number} correctly")
    print(f'now note the number you want the computer to guess"the number should  be in the range 1 too {x}"')
(guess(x))
def computer_guess(x):
    low = 1
    high = x
    feedback=""
    while feedback != "c" and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high bc low = high
        feedback = input(f"is {guess} too high (h), too low (l), or correct(c)?? ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("yeah! guess correctly")
    print("Congrats to both of you. You both made it....")
computer_guess(x)
print("for your wins lets do maths")
num1 = float(input("enter a number"))
num2 = float(input("enter an other number"))
print(f"{num1}+{num2}=",num1+num2, f"\n{num1}*{num2}=",num1*num2, f"\n{num1}-{num2}=",num1-num2, f"\n{num1}/{num2}=",num1/num2,)
print(f"thank you {name.upper()} for playing")
print("My first 41 lines of code!!!!!   hmmmmmmmm......")