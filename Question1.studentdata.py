Student_name ="Devika"
Student_id = "AS23"
Student_age = 23
Student_required_classes = True
marks = [78,90,67,89,59]
subjects=("Maths","Physics","Biology","Chemistry","Ai")
dict ={"Maths": 78,"Physics": 90, "Biology": 67, "Chemistry": 89, "Ai": 59}
print(f"Student Name:{Student_name}\nStudent ID:{Student_id}\nStudent Age:{Student_age}\nAttended all classes:{Student_required_classes}")
print( dict )
total_marks = sum(marks)
print("Total Marks  :",total_marks )
average_marks = total_marks/5
print("Average mark  :", average_marks)


