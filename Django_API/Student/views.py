from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt #Process the request without CSRF protection
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Student.models import Students,Subjects,Grades
from Student.serializers import StudentsSerializer,SubjectsSerializer,GradesSerializer

# Create your views here.

######################### Student CRUD #########################

@csrf_exempt
def studentAPI (request,id=0):

    if request.method=='GET': #read
       students = Students.objects.all()
       students_serializer= StudentsSerializer(students,many=True)
       return JsonResponse(students_serializer.data,safe=False)
    
    elif request.method=='POST': #create
        student_data= JSONParser().parse(request)
        students_serializer= StudentsSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Successfully created!",safe=False)
        return JsonResponse("Failed to create",safe=False)
    
    elif request.method=='PUT': #update
        student_data= JSONParser().parse(request)
        student = Students.objects.get(StudentID=student_data['StudentID'])
        students_serializer= StudentsSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Successfully updated!",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE': #delete
        student=Students.objects.get(StudentID=id)
        student.delete()
        return JsonResponse("Successfully deleted!",safe=False)

###################################################################

########################### Subject CRUD ##########################

@csrf_exempt
def subjectAPI (request,id=0):

    if request.method=='GET': #read
       subjects = Subjects.objects.all()
       subjects_serializer= SubjectsSerializer(subjects,many=True)
       return JsonResponse(subjects_serializer.data,safe=False)
    
    elif request.method=='POST': #create
        subject_data= JSONParser().parse(request)
        subjects_serializer= SubjectsSerializer(data=subject_data)
        if subjects_serializer.is_valid():
            subjects_serializer.save()
            return JsonResponse("Successfully created!",safe=False)
        return JsonResponse("Failed to create",safe=False)
    
    elif request.method=='PUT': #update
        subject_data= JSONParser().parse(request)
        subject = Subjects.objects.get(SubjectID=subject_data['SubjectID'])
        subjects_serializer= SubjectsSerializer(subject,data=subject_data)
        if subjects_serializer.is_valid():
            subjects_serializer.save()
            return JsonResponse("Successfully updated!",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE': #delete
        subject=Subjects.objects.get(SubjectID=id)
        subject.delete()
        return JsonResponse("Successfully deleted!",safe=False)
    
###################################################################

########################### Grade CRUD ############################
    
@csrf_exempt
def gradeAPI (request,id=0):

    if request.method=='GET': #read
       grades = Grades.objects.all()
       grades_serializer= GradesSerializer(grades,many=True)
       return JsonResponse(grades_serializer.data,safe=False)
    
    
    elif request.method == 'POST':  # create
        grade_data = JSONParser().parse(request)
        student_id = grade_data.pop('Student_id', None)
        subject_id = grade_data.pop('Subject_id', None)

        student = get_object_or_404(Students, pk=student_id)
        subject = get_object_or_404(Subjects, pk=subject_id)

        grades_serializer = GradesSerializer(data=grade_data)
        if grades_serializer.is_valid():
            grade = grades_serializer.save(Student=student, Subject=subject)
            return JsonResponse("Successfully created!", safe=False)
        return JsonResponse(grades_serializer.errors, status=400)
    
    elif request.method=='PUT': #update
        grade_data= JSONParser().parse(request)
        grade = Grades.objects.get(GradeID=grade_data['GradeID'])
        grades_serializer= GradesSerializer(grade,data=grade_data)
        if grades_serializer.is_valid():
            grades_serializer.save()
            return JsonResponse("Successfully updated!",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE': #delete
        grade=Grades.objects.get(GradeID=id)
        grade.delete()
        return JsonResponse("Successfully deleted!",safe=False)
    