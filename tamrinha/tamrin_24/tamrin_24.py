class Human:
    def __init__(self, name="", age=0, height=0.0, weight=0.0, national_id=""):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.national_id = national_id

    def display_human_info(self):
        print("\n-----------------------------")
        print("Personal Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")
        print(f"National ID: {self.national_id}")


class Student(Human):
    def __init__(self, name="", age=0, height=0.0, weight=0.0,
                 national_id="", student_id="", Course_of_study="", field_code="", degree="", entry_year=""):
        super().__init__(name, age, height, weight, national_id)
        self.student_id = student_id
        self.Course_of_study = Course_of_study
        self.field_code = field_code
        self.degree = degree
        self.entry_year = entry_year

    def display_student_info(self):
        self.display_human_info()
        print("\nStudent Information:")
        print(f"Student ID: {self.student_id}")
        print(f"Course of Study: {self.Course_of_study}")
        print(f"Field Code: {self.field_code}")
        print(f"Degree: {self.degree}")
        print(f"Entry Year: {self.entry_year}")
        print("-----------------------------")


data = {
    'name': 'MohammadMehdiSharifinia',
    'age': 22,
    'height': 175,
    'weight': 80,
    'national_id': '5560746193',
    'student_id': '02120040709007',
    'Course_of_study': 'Control',
    'field_code': '709',
    'degree': 'Bachelor',
    'entry_year': '021'
}

student = Student(**data)
student.display_student_info()
