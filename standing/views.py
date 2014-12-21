# -*- coding:utf-8 -*-
from django.shortcuts import render
from status.models import Status
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    all_submissions = Status.objects.all()

    standing = defaultdict( defaultdict() )
    
    list_standing = [ 'team_10' : { 'A' : 10 }, { 'B' : 40 } ]
    return render(request, 'index.html', {'list_standing':list_standing})


