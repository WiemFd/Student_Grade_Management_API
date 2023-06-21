from django.db import models

# Create your models here.

class Students(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DateOfBirth = models.DateField()

class Subjects(models.Model):
    SubjectID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Coefficient = models.IntegerField()

class Grades(models.Model):
    Student = models.ForeignKey (Students, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Value = models.DecimalField(max_digits=5, decimal_places=2)
