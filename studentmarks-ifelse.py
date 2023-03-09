subject1=float(input("Enter the Marks of Subject1-->"))
subject2=float(input("Enter the marks of Subject2-->"))
subject3=float(input("Enter the Marks of Subject3-->"))
total=subject1+subject2+subject3
avg=total/3

if avg>80:
    print("Distinction")
elif(avg>70):
        print("First Class")
elif(avg>60):
        print("Second Class")
elif(avg>40):
    print("Third Class")
else:
    print("You have Failed the Examination")