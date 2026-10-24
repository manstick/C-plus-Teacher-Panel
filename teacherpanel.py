import time
import random
import sys


#Teacher Panel Code -STICKMAN

students = [
        "Alex", "Anna", "Arda", "Charlotte", "Daniel", 
        "Emily", "Jack", "James", "Liam", "Lucas", 
        "Mert", "Mia", "Oliver", "Sophia", "William"
    ]
#values

min_l=1
max_l=20
choice=0


'''
The normal menu is for more short things like add or remove one stdudent, sort them etc.
But options menu is designed to do more moderations like remove the whole list and make another.
'''
def menu():
    global choice
    print()
    print("------Options-------")
    print()
    print("1.Add Student")
    print("2.Delete Student")
    print("3.Choose a random student")
    print("4.Sort all the students by name.")
    print("5.Options")
    print("6.Exit")
    print()
    choice=input("Select an Option = ") 
    print()

def options_menu():
    global o_choice, min_l, max_l, students,ad_student
    a=0
    o_choice=False
    print()
    print("|--Settings--|")
    print()
    print("1.Change min charachter number in name.")
    print("2.Change max charachter number in name.")
    print("3.Put you own list or add more than one students.")
    print("4.Clear the list")
    print()
    o_choice=input("Select an option = ")
    
    if o_choice=="1":
        min_l=int(input("Enter the min number = "))
    elif o_choice=="2":
        min_l=int(input("Enter the max number = "))
    elif o_choice=="3":
        i=int(input("How many students you want to add? = "))
        for i in range(0,i+1):
            a+=1
            ad_student=input("Enter the student name you want to add = ")
            students.append(ad_student)
            print(f"Student {ad_student} successfully added on the = {a}")
        print("Multiple adding is finished!")
        time.sleep(3)
               
    elif o_choice=="4":
        students.clear()
        print("Students list cleared")
        time.sleep(3)
def choose_r_std():
    random.randint(students)

while choice!=6:
    choice=0
    i=0
    ad_student=False
    delete_student=False
    
    print("Teacher Control Panel")
    
    print("---Students list---")
    for student in students:
        i+=1
        print(i,"-",student)
        
    menu()
    
    if choice=="1":
        ad_student=True
        ad_student=input("Enter the student name you want to add = ")
        if ("1" or "2" or "3" or "5" or "6" or "7" or "0" or "8" or "9") in ad_student:
                print("You entered a number please try again")
                time.sleep(2)
                continue
        elif len(ad_student)<=min_l or len(ad_student)>=max_l:
            print("You entered an invalid name")
        else:
            students.append(ad_student)
            print(f"Student {ad_student} successfully added on the = {i+1}")
        time.sleep(3)
            
    elif choice=="2":
        try:
            delete_student=input("Enter the student you want to delete = ")
            students.remove(delete_student)
        except:
            if len(students)==0:
                print("There is no enough students here add some!")
            else:
                print(f"Error: there is no student called {delete_student}")
        time.sleep(3)
    elif choice=="3":
        if len(students)==0:
            print("There is no enough students here add some!")
            time.sleep(3)
        else:
            choosen_num=random.randint(0,len(students)-1)
            choosen_student = students[choosen_num]
            print(f"Choosen student is = {choosen_student}")
            time.sleep(3)
    elif choice=="4":
        if len(students)==0:
            print("There is no enough student here add some!")
        else:  
            students.sort()
            print("Students have sorted automatically by alphabetical order!")
        time.sleep(3)
    elif choice=="5":
        options_menu()
    elif choice=="6":
        print("")
        break
sys.exit()