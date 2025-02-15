import json
import os
from models.student import Student

DATA_FILE = "data/students.json"

class StudentController:
  def __init__(self):
      self.students = []
      self.ensure_data_file()
      self.load_students()

  def ensure_data_file(self):
      """Ensure students.json exists."""
      if not os.path.exists("data"):
          os.makedirs("data")
      if not os.path.exists(DATA_FILE):
          with open(DATA_FILE, "w") as file:
              json.dump([], file)

  def load_students(self):
      """Load students from JSON file."""
      try:
          with open(DATA_FILE, "r") as file:
              data = json.load(file)
              self.students = [Student(s["name"], s["age"]) for s in data]
      except (FileNotFoundError, json.JSONDecodeError):
          self.students = []

  def save_students(self):
      """Save students to JSON file."""
      with open(DATA_FILE, "w") as file:
          json.dump([{"name": s.name, "age": s.age} for s in self.students], file, indent=4)

  def add_student(self, name: str, age: int):
      if not name.strip():
          print("Error: Student name cannot be empty.")
          return
      if age <= 0:
          print("Error: Age must be a positive number.")
          return
      student = Student.create_student(name, age)
      self.students.append(student)
      self.save_students()
      print(f"Student {name} added successfully!")

  def view_students(self):
      if not self.students:
          print("No students available.")
      for idx, student in enumerate(self.students, start=1):
          print(f"{idx}. {student.view_student()}")

  def edit_student(self, index: int, name: str = None, age: int = None):
      if 0 <= index < len(self.students):
          if name and not name.strip():
              print("Error: Name cannot be empty.")
              return
          if age is not None and age <= 0:
              print("Error: Age must be a positive number.")
              return
          self.students[index].edit_student(name, age)
          self.save_students()
          print("Student updated successfully!")
      else:
          print("Error: Invalid student index.")

  def delete_student(self, index: int):
      if 0 <= index < len(self.students):
          confirm = input(f"Are you sure you want to delete {self.students[index].name}? (yes/no): ").strip().lower()
          if confirm == "yes":
              del self.students[index]
              self.save_students()
              print("Student deleted successfully!")
          else:
              print("Deletion canceled.")
      else:
          print("Error: Invalid student index.")