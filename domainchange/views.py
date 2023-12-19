from django.shortcuts import render,redirect,reverse
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from teacher import models as TMODEL
from student import models as SMODEL
from teacher import forms as TFORM
from student import forms as SFORM
from django.contrib.auth.models import User
from .models import domain

def domain_view(request):
    domains=domain.objects.all()
    return render(request,"domainchange/domainchange.html",{"domains":domains})
def aws_view(request):
    return render(request,"domainchange/roadmap/AWS CC.html")
def azure_view(request):
    return render(request,"domainchange/roadmap/Azure CC.html")
def datascience_view(request):
    return render(request,"domainchange/roadmap/DataScience.html")
def deeplearning_view(request):
    return render(request,"domainchange/roadmap/deeplearning.html")
def devops_view(request):
    return render(request,"domainchange/roadmap/DevOps.html")
def webdev_view(request):
    return render(request,"domainchange/roadmap/Web Development using HTML, CSS, JavaScript .html")
def mern_view(request):
    return render(request,"domainchange/roadmap/Web Development Using MERN STACK.html")
def mevn_view(request):
    return render(request,"domainchange/roadmap/Web Development Using MEVN STACK.html")
def mean_view(request):
    return render(request,"domainchange/roadmap/Web Development Using MEAN STACK .html")




    
