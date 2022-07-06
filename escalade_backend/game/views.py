import random
import string
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from json import dumps
from registration.forms import ParticipantForm, TeamForm
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        TeamName = request.POST['TeamName']
        password=request.POST['password']

        team = auth.authenticate(teamName=TeamName, password=password)
        
        if team is not None :
            auth.login(request, team)
            print("logged in successfully")
            return redirect('/start')
        
        else:
            messages.info(request, "Invalid Credentials")
            print("lmao")
            return redirect('/')
    
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def start(request):
    team=request.user
    print(team.teamName)
    return render(request, 'registration/start.html', {'teamname':team.teamName})