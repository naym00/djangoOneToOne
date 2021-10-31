from django.db import models


# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    semester = models.CharField(max_length=5)
    phoneNumber = models.CharField(max_length=15, unique=True)
    age = models.IntegerField(blank=True, null=True, default=20)

    GENDER_CHOICES = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('TRANS_GENDER', 'TRANS GENDER')]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='MALE')

    def __str__(self):
        return self.semester + " -> " + self.firstName + " " + self.lastName


class RegistrationID(models.Model):
    studentID = models.CharField(max_length=20, unique=True)
    studentRoll = models.CharField(max_length=5)
    idFrom_Student_RegistrationID = models.OneToOneField(Student, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.idFrom_Student_RegistrationID.firstName + " " + self.studentID
