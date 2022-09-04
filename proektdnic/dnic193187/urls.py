from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('h', views.home, name="h"),
    path('signup',views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('lectures', views.lectures, name="lectures"),
    path('l1', views.l1, name="l1"),
    path('l2', views.l2, name="l2"),
    path('l3', views.l3, name="l3"),
    path('l4', views.l4, name="l4"),
    path('l5', views.l5, name="l5"),

    path('test', views.test, name="test"),
    path('t1', views.t1, name="t1"),
    path('t2', views.t2, name="t2"),
    path('t3', views.t3, name="t3"),
    path('t4', views.t4, name="t4"),
    path('t5', views.t5, name="t5"),

]
