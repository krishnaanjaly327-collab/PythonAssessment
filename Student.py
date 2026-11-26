from abc import ABC

class Student(ABC):
    def __init__(self,student_name,student_id,marks,attendence_status):
        self.student_name =student_name
        self.student_id =student_id
        self._marks = marks
        self.attendence_status = attendence_status

    def display_details(self):
        pass

    


       