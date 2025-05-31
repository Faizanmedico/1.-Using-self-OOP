class Student:
    def __init__(self, name, marks):
        """
        Constructor to initialize Student object.

        Args:
            name (str): The name of the student.
            marks (int): The marks obtained by the student.
        """
        self.name = name
        self.marks = marks

    def display(self):
        """
        Displays the name and marks of the student.
        """
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

# Create an instance of the Student class
student1 = Student("Sultan", 60)

# Call the display method to print student details
student1.display()

print("-" * 20) # Separator

student2 = Student("Ahmed", 63)
student2.display()