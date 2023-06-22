import pytest
from django.urls import reverse
from rest_framework import status
from Student.models import Subjects

############################################ Get test - read ###########################################
@pytest.mark.django_db
def test_subject_api_get(client):
    response = client.get(reverse('subjectAPI')) # url name in Student.urls
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == Subjects.objects.count()

############################################ Post test - create #########################################

@pytest.mark.django_db
def test_subject_api_post(client):
    subject_data = {
        "SubjectID": 216,
        "Name": "Linux",
        "Coefficient": 4
    }
    response = client.post(reverse('subjectAPI'), subject_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Put test - update #########################################

@pytest.mark.django_db
def test_subject_api_put(client):

    # Create a subject object new_subject
    new_subject = Subjects.objects.create(
        SubjectID= 902,
        Name= "Space Culture",
        Coefficient= 5
    )

    # Update this subject object new_subject
    subject_data = {
        "SubjectID": new_subject.SubjectID,
        "Name": "Marketing",
        "Coefficient": 1
    }
    subject_id = subject_data["SubjectID"]
    response = client.put(reverse('subject_detail', args=[subject_id]), subject_data, format='json')
    assert response.status_code == status.HTTP_200_OK

############################################ Delete test - delete #########################################

@pytest.mark.django_db
def test_subject_api_delete(client):

    # Create a subject object new_subject
    new_subject = Subjects.objects.create(
        SubjectID= 902,
        Name= "Space Culture",
        Coefficient= 5
    )

    subjectID = new_subject.SubjectID
    response = client.delete(reverse('subject_detail', args=[subjectID]))
    assert response.status_code == status.HTTP_200_OK
    assert Subjects.objects.count() == 0
