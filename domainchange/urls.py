from django.urls import path,include
from . import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
app_name="domain"
urlpatterns = [
   
    path('',views.domain_view,name= "domainchange"),
    path('aws',views.aws_view,name= "aws"),
    path('azure',views.azure_view,name= "azure"),
    path('datascience',views.datascience_view,name= "datascience"),
    path('deeplearning',views.deeplearning_view,name= "deeplearning"),
    path('devops',views.devops_view,name= "devops"),
    path('webdev',views.webdev_view,name= "webdev"),
    path('mern',views.mern_view,name= "mern"),
    path('mevn',views.mevn_view,name= "mevn"),
    path('mean',views.mean_view,name= "mean"),
    
]