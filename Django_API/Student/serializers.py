from rest_framework import serializers 
from Student.models import Students,Subjects,Grades

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('StudentID','FirstName','LastName','DateOfBirth')

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields=('SubjectID','Name','Coefficient')

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grades
        fields=('GradeID','Value','Student_id','Subject_id')