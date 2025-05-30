class Human:
    def __init__(self, name, age, height, weight, national_id):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.national_id = national_id

    def get_info(self):
        return (
            f"\n--- Personal Info ---\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Height: {self.height} cm\n"
            f"Weight: {self.weight} kg\n"
            f"National ID: {self.national_id}"
        )


class Student(Human):
    def __init__(self, name, age, height, weight, national_id,
                 student_id, course, field_code, degree, entry_year):
        super().__init__(name, age, height, weight, national_id)
        self.student_id = student_id
        self.course = course
        self.field_code = field_code
        self.degree = degree
        self.entry_year = entry_year

    def get_info(self):
        return (
            super().get_info() +
            f"\n--- Student Info ---\n"
            f"Student ID: {self.student_id}\n"
            f"Course: {self.course}\n"
            f"Field Code: {self.field_code}\n"
            f"Degree: {self.degree}\n"
            f"Entry Year: {self.entry_year}\n"
        )


student = Student('MohammadMehdiSharifinia', 22, 175, 80, 5560746193,'02120040709007', 'Control', 709, 'Bachelor', '021')

print(student.get_info())
