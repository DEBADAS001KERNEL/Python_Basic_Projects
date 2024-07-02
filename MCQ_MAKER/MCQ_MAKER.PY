
mcq_dict={}
print("WELCOME TO MCQ MAKER APP : ")
C=int(input("PLEASE ENTER HOW MANY QUESTION YOU NEED : "))
for i in range(0,C):
    q=input(f"PLEASE ENTER THE QUESTION NO {i}  : ")
    a=input(f"PLEASE ENTER THE ANS FOR QUESTION NO {i}  : ")
    mcq_dict.update({q:a})


k = 0
score = 0
questions = list(mcq_dict.keys())
answers = list(mcq_dict.values())

while k < C:
    print(questions[k])
    ans1 = input("WRITE YOUR ANSWER: ")
    if ans1 == answers[k]:
        print("CORRECT ANSWER!!...+1")
        score += 1
    else:
        print("WRONG. SORRY...-1")
        score -= 1
    k += 1

print(f"YOUR FINAL SCORE IS: {score}")