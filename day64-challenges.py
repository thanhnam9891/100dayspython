class job():
    def __init__(self,name,salary,workinghour):
        self.name = name
        self.salary=salary
        self.workinghour=workinghour

    def show(self):
        print(f"Job title:{self.name}\nSalary: {self.salary}\nWorking Hour:{self.workinghour} hours")

class doctor(job):
    def __init__(self, speciality,year):
        self.name = "Doctor"
        self.salary = "Doing very nicely thank you"
        self.workinghour = 50
        self.speciality=speciality
        self.year = year
    
    def display(self):
        print(f"Job title:{self.name}\nSalary: {self.salary}\nWorking Hour:{self.workinghour} hours\nYear:{self.year}")

    
class teacher(job):
    def __init__(self,subject,position):
        self.name = "Teacher"
        self.salary = "Nowhere near enough"
        self.workinghour = "All of them"
        self.subject = subject
        self.position= position
    def display(self):
        print(f"Job title:{self.name}\nSalary: {self.salary}\nWorking Hour:{self.workinghour} hours\nSubject: {self.subject}\nPosition: {self.position}")

lawyer = job("Lawyer","600,000 USD",100)
lawyer.show()
compteacher = teacher("Computer Science","Classroom Teacher")
compteacher.display()
doctor = doctor("Pediatric Consultant",7)
doctor.display()