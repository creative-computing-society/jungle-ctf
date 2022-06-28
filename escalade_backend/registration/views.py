import random
import string
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from registration.forms import ParticipantForm, TeamForm


# Create your views here.

def index(request):
    return HttpResponse("homepage")

def register(request):

    if request.method=="POST":
        
        #generate password
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        
        #validating team name
        teamData = {
            'teamName': request.POST['teamName'],
            'password': password
        }
        form = TeamForm(teamData)
        if not form.is_valid():
            messages.error(request, "Team name taken")
            return redirect("/register")
        
        #validating leader details
        leaderData = {
            'name': request.POST["leaderName"],
            'email': request.POST["leaderEmail"],
            'rollno': request.POST["leaderRollNo"],
            'discord_ID': request.POST["leaderDiscord"],
        }
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            for key in leaderForm.errors:
                messages.error(request, f"{strip_tags(leaderForm.errors[key])} for Team Leader")
            return redirect("/register")
        
        #validating memeber 1 details
        m1Data = {
            'name': request.POST["m1Name"],
            'email': request.POST["m1Email"],
            'rollno': request.POST["m1RollNo"],
            'discord_ID': request.POST["m1Discord"],
        }
        m1Form = ParticipantForm(m1Data)
        if not m1Form.is_valid():
            for key in m1Form.errors:
                messages.error(request, m1Form.errors[key])
            return redirect("/register")
        
        if request.POST["m2Email"]!="":
            #validating member2 details if present
            m2Data = {
                'name': request.POST["m2Name"],
                'email': request.POST["m2Email"],
                'rollno': request.POST["m2RollNo"],
                'discord_ID': request.POST["m2Discord"],
            }
            m2Form = ParticipantForm(m2Data)
            if not m2Form.is_valid():
                for key in m2Form.errors:
                    messages.error(request, m2Form.errors[key])
                return redirect("/register")
        
        to_list = [request.POST['leaderEmail'], request.POST['m1Email']]

        #add leader email to team
        teamData['email'] = request.POST['leaderEmail']
        team = TeamForm(teamData).save()   #save team
        
        leaderData['team'] = team
        ParticipantForm(leaderData).save()  #save leader
        
        m1Data['team'] = team
        ParticipantForm(m1Data).save()  #save member1
        
        if request.POST["m2Email"]!="":
            to_list.append(request.POST["m2Email"])
            m2Data['team'] = team
            ParticipantForm(m2Data).save()  #save member2

        #TODO: send emails
        # subject = "Thank you for registering!"
        # password={'OTP':password,'Team_Name': teamData['teamName']} #password dict to be passed to email template
        # html_message = render_to_string('registration/registrationsuccessful.html', password) #html rendered message
        # message = strip_tags(html_message) #incase html render fails
        # from_email = settings.EMAIL_HOST_USER
        # send_mail(subject, message, from_email, to_list, html_message=html_message, fail_silently=False)
        
        
        return HttpResponse("success")

    return render(request, "registration/register.html")