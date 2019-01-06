"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from main import views

urlpatterns = [
      url ('downvote/',views.downvote),
      url ('upvote/',views.upvote),
      url('answer/',views.answer),
      url('question/',views.question),
      url('dashboard/',views.dashboard),
      url('login/',views.login),
      url('signup/',views.signup),
       url('test/',views.test),
       url('',views.homePageView),

#url('hello/',views.hello,name='hello'),
#url('',views.homePageView,name='home'),

]

