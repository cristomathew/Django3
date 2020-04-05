from django.urls import path
from . import views
urlpatterns = [
    path('',views.resultlist,name="resultlist"),
    path('<int:pk>/',views.resultview,name="resultsview"),
]