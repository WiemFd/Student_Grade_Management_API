from django.urls import path
from Student import views

urlpatterns=[
    path('student',views.studentAPI),
    path('student/<int:id>',views.studentAPI),

    path('subject',views.subjectAPI),
    path('subject/<int:id>',views.subjectAPI),

    path('grade',views.gradeAPI),
    path('grade/<int:id>',views.gradeAPI),
]