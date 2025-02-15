from config import MAX_NAME_LENGTH

class Student:
  def __init__(self, name: str, age: int) -> None:
    """
      Initialize a new student

      Args:
        name (str): The name of the student
        age (int): The age of the student

      Raises:
        ValueError: If the name is empty or exceeds
        MAX_NAME_LENGTH
    """
    if not name:
      raise ValueError("Name cannot be empty.")
    if len(name) > MAX_NAME_LENGTH:
      raise ValueError(f"Name cannot be more than {MAX_NAME_LENGTH} characters.")

    self.name = name
    self.age = age

  # Methods
  def view_student(self) -> str:
    """Return a string representation of the student's details."""
    return f"Student Name: {self.name}, Age: {self.age}"

  def edit_student(self, name: str = None, age: int = None) -> None:
    """Edit the student's name and age."""
    if name:
      if len(name) > MAX_NAME_LENGTH:
        raise ValueError(f"Name cannot be more than {MAX_NAME_LENGTH} characters.")
      self.name = name
    if age:
      self.age = age

  def delete_student(self) -> None:
    """Delete the student's data by setting attributes to None."""
    self.name = None
    self.age = None

  @classmethod
  def create_student(cls, name: str, age: int):
    """Create and return a new student instance."""
    return cls(name, age)
