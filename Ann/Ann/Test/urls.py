from django.urls import path
from . import views
urlpatterns = [
    path('',views.test,name="test"),
    path('list/',views.testlist,name="testlist"),
    path('<int:pk>/',views.viewtest,name="viewtest"),
]