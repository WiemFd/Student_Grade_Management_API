import pytest
from django.urls import reverse
from rest_framework import status
from Student.models import Grades,Students,Subjects

############################################ Get test - read ###########################################
@pytest.mark.django_db
def test_grade_api_get(client):
    response = client.get(reverse('gradeAPI')) # url name in Student.urls
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == Grades.objects.count()

############################################ Post test - create #########################################

@pytest.mark.django_db
def test_grade_api_post(client):
        
    # Create a subject object new_subject
    new_subject = Subjects.objects.create(
        SubjectID= 902,
        Name= "Space Culture",
        Coefficient= 5
    )
    # Create a student object new_student
    new_student = Students.objects.create(
        StudentID=14782139,
        FirstName="Maria",
        LastName="Alexander",
        DateOfBirth="1995-08-15"
    )
    grade_data = {
        "GradeID": 1,
        "Value": "1.5",
        "Student_id": new_student.StudentID,
        "Subject_id": new_subject.SubjectID
    }
    response = client.post(reverse('gradeAPI'), grade_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Put test - update #########################################

@pytest.mark.django_db
def test_grade_api_put(client):

    # Create a subject object new_subject
    new_subject = Subjects.objects.create(
        SubjectID= 902,
        Name= "Space Culture",
        Coefficient= 5
    )
    # Create a student object new_student
    new_student = Students.objects.create(
        StudentID=14782139,
        FirstName="Maria",
        LastName="Alexander",
        DateOfBirth="1995-08-15"
    )
    # Create a grade object new_grade
    new_grade = Grades.objects.create(
        GradeID= 2,
        Value= "10.50",
        Student_id= new_student.StudentID,
        Subject_id= new_subject.SubjectID
    )

    # Update this grade object new_grade
    grade_data = {
        "GradeID": new_grade.GradeID,
        "Value": "6.50",
        "Student_id": new_student.StudentID,
        "Subject_id": new_subject.SubjectID
    }
    grade_id = grade_data["GradeID"]
    response = client.put(reverse('grade_detail', args=[grade_id]), grade_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Delete test - delete #########################################

@pytest.mark.django_db
def test_grade_api_delete(client):

    # Create a grade object new_grade
    new_grade = Grades.objects.create(
        GradeID= 2,
        Value= "10.50",
        Student_id= 14795167,
        Subject_id= 517
    )

    gradeID = new_grade.GradeID
    response = client.delete(reverse('grade_detail', args=[gradeID]))
    assert response.status_code == status.HTTP_200_OK
    assert Grades.objects.count() == 0
