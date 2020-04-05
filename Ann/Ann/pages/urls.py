from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.loginuser,name="loginuser"),
    path('signup/',views.signupuser,name="signupuser"),
    path('logout/',views.logoutuser,name="logout"),
]