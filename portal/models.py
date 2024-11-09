from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Any other fields related to teacher

    def __str__(self):
        return f"{self.user.username} - Teacher"


class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10)

    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
