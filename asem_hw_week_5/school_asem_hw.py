class School:
    def __init__(self, name, foundation_year,students,teachers):
        self.name=name
        self.foundation_year=foundation_year
        self.students=students
        self.teachers=teachers

    
    def add_new_student(self, student_name,student_class):
         new_entry={"name": student_name, "class": student_class}
         self.students.append(new_entry)
    def add_new_teacher(self,teacher_name,branch_name):
        self.teachers[teacher_name] = branch_name
    def view_student_list(self):
         print("Student List:")
         for student in self.students:
              print(f"- {student['name']} (Class: {student['class']})")
    def view_teacher_list(self):
          print("Teacher List:")
          for name, branch in self.teachers.items():
                     print(f"- {name} (Major: {branch})")


my_school = School("Debrecen", 2019, [],{})

#  Add student
my_school.add_new_student("Ali", "Grade 5")
my_school.add_new_student("Lina", "Grade 8")
my_school.add_new_student("Mike", "Grade 4")





# Add teacher
my_school.add_new_teacher("Mr.Wood", "programing 1")
my_school.add_new_teacher("Ms.Sarah", "Science")



# View students
my_school.view_student_list()

# View teachers
my_school.view_teacher_list()








