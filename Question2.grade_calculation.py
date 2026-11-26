mark=int(input("Enter your mark"))
attendence =int(input("Enter your attendence"))

if(mark>=90):
    print("A")
elif(mark>=80 and mark<90):
    print("B")
elif(mark>=70 and mark<80):
    print("C")
elif(mark>=60 and mark<70):
    print("D")
elif(mark>=50 and mark<60):
    print("E")
elif(mark<50):
    print("F")
elif(mark>=40):
    print("Pass")
else:
    print("Fail")
if(attendence<75 and mark>=40):
    print("Attendence Shortage ")
    print("Not Passed")





