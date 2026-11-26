from Student import Student

class Average(Student):
    def __init__(self, student_name, student_id, marks, attendence_status):
        # super().__init__(student_name, student_id, marks, attendence_status) 
        self._marks = marks
           
    def calculate_average(self):
        Avg =  self._marks/5
        
 