import random as r
import pyfiglet

print(pyfiglet.figlet_format("PASS__GEN_._V_._1"))

upper_case = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

num = ['1', '2', '3', '4', '5', '6', '7', '8', '0', '0']

sp = ['!', '@', '#', '£', '$', '%', '^', '&', '*', '*', ';', ':', '?']

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

UPP_letter = int(input("How many uppercase letters do you need: "))
LOW_letter = int(input("How many lowercase letters do you need: "))
number = int(input("How many numbers do you need: "))
spacial = int(input("How many special characters do you need: "))

p1 = ""

for n in range(1, UPP_letter + 1):
    la = r.choice(upper_case)
    p1 += la

p2 = ""

for n in range(1, LOW_letter + 1):
    la = r.choice(lower_case)
    p1 += la

p3 = ""

for n in range(1, number + 1):
    nu = r.choice(num)
    p2 += nu

p4 = ""

for n in range(1, spacial + 1):
    s = r.choice(sp)
    p3 += s

T = "Your generated password is: " + p1 + p2 + p3 + p4
print(T)
print(pyfiglet.figlet_format(p1 + p2 + p3 + p4))
