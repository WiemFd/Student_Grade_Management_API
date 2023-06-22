import pytest
from django.urls import reverse
from rest_framework import status
from Student.models import Students

############################################ Get test - read ###########################################
@pytest.mark.django_db
def test_student_api_get(client):
    response = client.get(reverse('studentAPI'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == Students.objects.count()

############################################ Post test - create #########################################

@pytest.mark.django_db
def test_student_api_post(client):
    student_data = {
        'StudentID': 14769850,
        'FirstName': 'Paolo',
        'LastName': 'Chirco',
        'DateOfBirth': '1990/04/01'
    }
    response = client.post(reverse('studentAPI'), student_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Put test - update #########################################

@pytest.mark.django_db
def test_student_api_put(client):

    # Create a student object new_student
    new_student = Students.objects.create(
        StudentID=14782139,
        FirstName="Maria",
        LastName="Alexander",
        DateOfBirth="1995-08-15"
    )

    # Update this student object new_student
    student_data = {
        "StudentID": new_student.StudentID,
        "FirstName": "Rosaa",
        "LastName": "alexander",
        "DateOfBirth": "1997-08-15"
    }
    student_id = student_data["StudentID"]
    response = client.put(reverse('student_detail', args=[student_id]), student_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Delete test - delete #########################################

@pytest.mark.django_db
def test_student_api_delete(client):
    # Create a student object new_student
    new_student = Students.objects.create(
        StudentID=14782139,
        FirstName="Maria",
        LastName="Alexander",
        DateOfBirth="1995-08-15"
    )

    studentID = new_student.StudentID
    response = client.delete(reverse('student_detail', args=[studentID]))
    assert response.status_code == status.HTTP_200_OK
    assert Students.objects.count() == 0
