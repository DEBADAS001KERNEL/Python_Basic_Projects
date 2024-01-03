
import pyfiglet
print(pyfiglet.figlet_format("TO_DO_DICT"))   #import libraries
print("Welcome To TO-DO Dictenory")




to_do={}
another_task='yes'

while(another_task=="yes"):

    Tiem = (input("Enter the time : "))
    Task = input("What You Want to Do :")              # task and time entry from user.
    to_do[Tiem] = Task

    another_task =input("IS there any other task: ")
    if(another_task=='yes'):
        continue

print("") # just for space

print(to_do)

file_name=input("Enter the name of the TO-DO LIST file: ")

with open(file_name, 'w') as file:
    for time, task in to_do.items():                                   # saving the todo list as a file.
        file.write(f"{time}: {task}\n")

print("To-Do list saved to : file_name")