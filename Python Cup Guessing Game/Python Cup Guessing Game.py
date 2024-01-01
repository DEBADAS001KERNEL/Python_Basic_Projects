import random
import pyfiglet

print(pyfiglet.figlet_format("Cup Guessing"))

# Taking a random number between 1 to 10
a = random.randint(1, 10)


cup1 = 0
cup2 = 0
cup3 = 0

c = ['cup1', 'cup2', 'cup3']

C = a
C = random.choice(c)


print("Rules: First, choose the correct cup that contains the number. After correctly guessing the cup, choose the correct number hidden under the cup.")
print("After choosing the correct number, you will be the winner.")

choose = input("Enter the name of the CORRECT cup: ")
print("")

if choose == C:
    print("HURRAY, Correct cup.")
    print(f"Yes, the cup is {C}")
    print("You have passed level-1")
    print("")

    choose_num = int(input("Now choose the Number: "))
    if choose_num == a:
        print("Correct guess.... Finally, you are the winner!")
    else:
        print("Game over.")
else:
    print("Wrong Choice")
    print("Game over. Better luck next time.")

