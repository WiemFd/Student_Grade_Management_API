from django.urls import path
from Student import views

urlpatterns=[
    path('student',views.studentAPI),
    path('student/<int:id>',views.studentAPI)
]