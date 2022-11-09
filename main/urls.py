from django.urls import path
from . import views

urlpatterns = [
    path("",views.blank,name = "blank"), #forlocal host
    path("main/",views.home,name="home"), #route
    path("register/",views.register,name="register"), #register route
    path("login/",views.login,name="login"), #login route
    path("logout",views.logout,name='logout'),
    path("dashboard/",views.dashboard,name="dashboard") #dashboard route
]