from django.urls import path
from . import views
urlpatterns=[
    path('get',views.EmployeeListCreateAPIView.as_view()),
    path('list/<int:id>/',views.EmployeeRetrieveUpdateDestroyAPIView.as_view())
]