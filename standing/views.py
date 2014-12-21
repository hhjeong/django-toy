# -*- coding:utf-8 -*-
from django.shortcuts import render
from standing.models import Status
from django import forms
from django.http import HttpResponseRedirect
from collections import defaultdict 
# Create your views here.

def index(request):
    all_submissions = Status.objects.all()

    standing = defaultdict( defaultdict )
    
    list_standing = [ ['team_10' , { 'A' : 10 ,  'B' : 40 }] ]

    print list_standing
    return render(request, 'standing.html', {'list_standing':list_standing})


