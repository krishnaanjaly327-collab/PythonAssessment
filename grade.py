from Student import Student

class grade(Student):
    def __init__(self, student_name, student_id, marks, attendence_status):
        super().__init__(student_name, student_id, marks, attendence_status) 
        self._marks = marks
           
    def calculate_grade(self):
        if(self._marks>=90):
            print("A")
        elif(self._marks>=80 and self._marks<90):
            print("B")
        elif(self._marks>=70 and self._marks<80):
            print("C")
        elif(self._marks>=60 and self._marks<70):
            print("D")
        elif(self._marks>=50 and self._marks<60):
            print("E")
        else:
            print("Fail")
