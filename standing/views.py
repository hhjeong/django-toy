# -*- coding:utf-8 -*-
from django.shortcuts import render
from standing.models import Status
from django import forms
from django.http import HttpResponseRedirect
from collections import defaultdict 
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    all_submissions = Status.objects.all()

    standing = defaultdict( int ) 

    for a in all_submissions:
        team_id = a.team_id
        prob_id = a.pid
        result = a.result

        if result == "YES":
            standing[team_id] += 1
        
    list_standing = standing.items()
    print list_standing
    return render(request, 'standing.html', {'list_standing':list_standing})


