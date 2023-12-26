import random as R # import random module

Num=R.randint(1,10) # take a number between 1 to 10
count=0

Guess_Num=int(input("Enter the Number Or guess the Number :"))# input the number
count=count+1
while(Guess_Num!=Num):
    if(Guess_Num<Num):
        print("you have  choosed  smaller number then the original number ")
        Guess_Num=int(input("Enter the Number Or guess the Number :"))                           # Full LOgic
        count=count+1
    elif(Guess_Num>Num):
        print("you have  choosed  bigger number then the original number ")
        Guess_Num=int(input("Enter the Number Or guess the Number :"))
        count=count+1 
           

print("HURRY...Correct")

print(f"You took {count} times ")

print(f"The Number is: {Num} ")           
    