from django.urls import path,include
from myproject import views




urlpatterns=[     
    path("",views.Main,name="main"),
    path("register/",views.register,name="register"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("book/",views.book,name="book"),
    path("contact/",views.contact,name="contact"),
    path("main/",views.Main,name="main"),
    path("group/", views.group, name="group"),
    path("indian/",views.indian,name="indian"),
    path("india/",views.india,name="india"),
    path("north/",views.north,name="north"),
    path("education/",views.education,name="education"),
    path("south/",views.south,name="south"),
    path("east/",views.east,name="east"),
    path("europe/",views.europe,name="europe"),
    path("honeymoon/",views.honeymoon,name="honeymoon"),
    path("description/",views.description,name="description"),
    path("def/<str:plan>",views.description_view,name="def"),

]