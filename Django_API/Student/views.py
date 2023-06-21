from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #Process the request without CSRF protection
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Student.models import Students,Subjects,Grades
from Student.serializers import StudentsSerializer,SubjectsSerializer,GradesSerializer

# Create your views here.
 
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
            return JsonResponse("successfully created!",safe=False)
        return JsonResponse("Failed to create",safe=False)
    
    elif request.method=='PUT': #update
        student_data= JSONParser().parse(request)
        student = Students.objects.get(StudentID=student_data['StudentID'])
        students_serializer= StudentsSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("successfully updated!",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE': #delete
        student=Students.objects.get(StudentID=id)
        student.delete()
        return JsonResponse("successfully deleted!",safe=False)