# -*- coding:utf-8 -*-
from django.shortcuts import render
from status.models import Status
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    all_submissions = Status.objects.all()[::-1]
    return render(request, 'index.html', {'all_submissions':all_submissions})

class submitForm(forms.Form):
    team_id = forms.CharField(max_length=4)
    pid = forms.CharField(max_length=1)

def submit(request):
    if request.method == "POST":

        form = submitForm(request.POST)

        if form.is_valid():
            t = form.cleaned_data['team_id']
            p = form.cleaned_data['pid']
           
            print t 
            s = Status(team_id=t,pid=p)
            s.save()
            return HttpResponseRedirect('/status/')

    else:
        form = submitForm()
        
        return render(request, 'submit.html', { 'form':form } )
    
