from django.db import models

# Create your models here.

class Students(models.Model):
    StudentID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DateOfBirth = models.DateField()
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Subjects(models.Model):
    SubjectID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Coefficient = models.IntegerField()
    def __str__(self):
        return self.Name

class Grades(models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Value = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.Student.FirstName} {self.Student.LastName} - {self.Subject.Name}"
