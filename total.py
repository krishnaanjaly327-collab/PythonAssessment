from Student import Student

class Total(Student):
    def __init__(self, student_name, student_id, marks, attendence_status):
        # super().__init__(student_name, student_id, marks, attendence_status) 
        self._marks = marks
           
    def calculate_total(self):
        Sum =  self._marks


        