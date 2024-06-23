# LET'S CREATE

w=["rock","paper","scissors"]
import random


i=1

while True:
    u=input("choose : ")
    c=random.choice(w)
    print(f"com choose  {c}")
    
    if(c=="rock" and u=="paper"):
        print(f"You win, cause You choose {u} and Com choose {c}")
        
        break
    elif(c=="paper" and u=="rock"):
        print(f"Com win, cause You choose {u} and Com choose {c}")
       
        break

    elif(c=="scissors" and u=="rock"):
        print(f"You win, cause You choose {u} and Com choose {c}")
        
        break
    elif(c=="rock" and u=="scissors"):
        print(f"Com win, cause You choose {u} and Com choose {c}")
        
        break

    elif(c=="paper" and u=="scissors"):
        print(f"You win, cause You choose {u} and Com choose {c}")
        
        break #
    elif(c=="scissors" and u=="paper"):
        print(f"Com win, cause You choose {u} and Com choose {c}")
       
        break

    else:
        print(f"chose 'rock','paper' or 'scissors'...... use lowercase..")

