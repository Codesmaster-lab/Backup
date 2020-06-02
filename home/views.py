from django.shortcuts import render
from Posts.models import New
from Users.models import User



def home(request):
    return render(request,'home/home.html',{ 'title' : 'Home','news':New.objects.all()})


def team(request):
    return render(request,'home/team.html',{ 'title' : 'Team','users':User.objects.all()})


