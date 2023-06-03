from django.urls import path
from.views import *
from fundapp import views


urlpatterns = [
     path('', views.index, name='index'),
     path("home/",views.home ),
     path("project/",views.project),
     path("register/",views.signup),
     path("base/",views.base),
     path('login',views.login),
     path('projectview/',views.projectview),
     path('donate/<int:pk>',views.donate),
     path('projectlist/',views.projectlist),
     path('about/',views.about),
     path('logout/',views.user_logout),
     path('pay',views.pay),
     path('money',views.money),
     path('payment',views.payment),
     path('category',views.category),
     path('projectshow/',views.projectshow),
     path('contactus/',views.contactus),
     path ('search/',views.searchproject,name="searchproject"),
     path('my/',views.contributions)

     ]