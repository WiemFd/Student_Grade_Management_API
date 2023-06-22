from django.urls import path
from Student import views

urlpatterns=[
    path('student', views.studentAPI, name='studentAPI'),
    path('student/<int:id>', views.studentAPI, name='student_detail'),

    path('subject', views.subjectAPI, name='subjectAPI'),
    path('subject/<int:id>', views.subjectAPI, name='subject_detail'),
    
    path('grade', views.gradeAPI, name='gradeAPI'),
    path('grade/<int:id>', views.gradeAPI, name='grade_detail'),
]