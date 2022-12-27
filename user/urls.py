from django.urls import path
from user import views
  
urlpatterns = [
    path("",views.home,name='home'),
    path("about/", views.about, name="about"),
    path("explore/", views.explore, name="explore"),
    path("contact/", views.contact, name="contact"),
    path("signin/", views.signin, name="signin"),
    path("login/", views.login, name="login"),
    path("userlogin/", views.user_login, name="userlogin"), 
    path("usersignin/", views.user_signin, name="usersignin"),
    path('login/addinfo/',views.addinfo,name="addinfo"),
     path("site/", views.mainlogin, name="site"),
]