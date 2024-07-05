class Amusement:
    
    def __init__(self):
        pass
    
    def detail(self, name, mob, ride, age, bill):
        self.name = name
        self.mob = mob
        self.ride = ride
        self.age = age
        self.bill = bill
        
        det = {"NAME": self.name, "MOBILE": self.mob, "RIDE": self.ride, "BILL": self.bill}
        a = {}
        a.update(det)
        print(a)

    def roller(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "roller coaster"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "20$"
        if age >= 18:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOU ARE TOO YOUNG FOR THIS RIDE")

    def water_ride(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "WATER RIDE"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "30$"
        if age >= 16:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOU ARE TOO YOUNG FOR THIS RIDE")

    def horror_train(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "HORROR TRAIN"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "35$"
        if age >= 18:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOU ARE TOO YOUNG FOR THIS RIDE") 

    def electric_car(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "ELECTRIC CAR"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "40$"
        if age >= 16:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOU ARE TOO YOUNG FOR THIS RIDE")  

    def merigo(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "MERRY-GO-ROUND"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "30$"
        if age >= 18:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOU ARE TOO YOUNG FOR THIS RIDE")

    def micky(self):
        name = input("PLEASE ENTER THE NAME: ")
        mob = input("PLEASE ENTER THE MOBILE NUMBER: ")
        ride = "MICKEY MOUSE"
        age = int(input("PLEASE ENTER THE AGE: "))
        bill = "15$"
        if 9 <= age <= 17:
            self.detail(name, mob, ride, age, bill)
        else:
            print("SORRY YOUR AGE IS NOT PERFECT FOR THIS RIDE")     

if __name__ == "__main__":
    while True:
        print("WELCOME TO THE AMUSEMENT PARK OPERATOR:")
        print("PRESS 1 FOR ROLLER COASTER:")
        print("PRESS 2 FOR WATER RIDE:")
        print("PRESS 3 FOR HORROR TRAIN:")
        print("PRESS 4 FOR ELECTRIC CAR:")
        print("PRESS 5 FOR MERRY-GO-ROUND:")
        print("PRESS 6 FOR MICKEY MOUSE:")
        print("PRESS 7 FOR EXIT:")
        c = input("PLEASE ENTER YOUR OPTION:")

        if c == "1":
            a = Amusement()
            a.roller()
        elif c == "2":
            a = Amusement()
            a.water_ride() 
        elif c == "3":
            a = Amusement()
            a.horror_train()
        elif c == "4":
            a = Amusement()
            a.electric_car()
        elif c == "5":
            a = Amusement()
            a.merigo()
        elif c == "6":
            a = Amusement()
            a.micky()
        else:
            break