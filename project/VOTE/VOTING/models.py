from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()  # Use DateField for date of birth
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    register_no = models.CharField(max_length=13)
    roll_no = models.CharField(max_length=9)
    department = models.CharField(max_length=100, default="ComputerScience")
    batch = models.CharField(max_length=15, default="2022-25")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Example of a custom method (optional)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Meta class to define additional settings
    class Meta:
        ordering = ['last_name']  # Sorting by last name by default

from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="ComputerScience")
    batch = models.CharField(max_length=15, default="2022-25")
    image = models.ImageField(upload_to="profilepic/")  # Field for profile picture
    position = models.CharField(max_length=100)  # Field for position

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
