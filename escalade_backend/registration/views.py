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

from registration.forms import ParticipantForm, TeamForm


# Create your views here.

def index(request):
    return HttpResponse("homepage")

@login_required(login_url="/admin/login/")
def deleteExpiredSession(request):
    request.session.clear_expired()
    return HttpResponse('Expired Sessions Deleted')

def teamRegister(request):
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
            messages.error(request, "Team name taken", extra_tags="teamName")
            return redirect('/team-register')

        leaderData = {
            'name': request.POST["leaderName"],
            'email': request.POST["leaderEmail"],
            'rollno': request.POST["leaderRollNo"],
            'phoneno': request.POST["leaderPhoneNo"],
            'discord_ID': request.POST["leaderDiscord"],
        }
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            for key in leaderForm.errors:
                messages.error(request, strip_tags(leaderForm.errors[key]), extra_tags=key)
            return redirect("/team-register")
        
        request.session['team'] = {
            'teamData': teamData,
            'leaderData': leaderData
        }
        request.session.set_expiry(3600)

        return redirect('/members-register')

    if request.session.get('team', False):
        del request.session['team']
    
    context = {}
    msgs = messages.get_messages(request)
    if msgs:
        for msg in msgs:
            context[msg.tags.replace(" ", "_")] = str(msg)
        msgs.used = True
    return render(request, 'registration/teamRegister.html', context=context)


def membersRegister(request):
    
    if request.method=='POST':
        teamData = request.session['team']['teamData']
        leaderData = request.session['team']['leaderData']

        form = TeamForm(teamData)
        if not form.is_valid():
            messages.error(request, "Team name taken", extra_tags="teamName")
            return redirect('/team-register')
        
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            for key in leaderForm.errors:
                messages.error(request, strip_tags(leaderForm.errors[key]), extra_tags=key)
            return redirect("/team-register")

        m1Data = {
            'name': request.POST["m1Name"],
            'email': request.POST["m1Email"],
            'rollno': request.POST["m1RollNo"],
            'phoneno': request.POST["m1PhoneNo"],
            'discord_ID': request.POST["m1Discord"],
        }
        m1Form = ParticipantForm(m1Data)
        if not m1Form.is_valid():
            for key in m1Form.errors:
                messages.error(request, strip_tags(m1Form.errors[key]), extra_tags=f"{key}1")
            return redirect("/members-register")
        duplicate_entry = False
        if m1Data['email']==leaderData['email']:
            messages.error(request, "Member 1 email is same as Leader email", extra_tags="email1")
            duplicate_entry = True
        if m1Data['rollno']==leaderData['rollno']:
            messages.error(request, "Member 1 Roll Number is same as Leader Roll Number", extra_tags="rollno1")
            duplicate_entry = True
        if m1Data['phoneno']==leaderData['phoneno']:
            messages.error(request, "Member 1 Phone Number is same as Leader Phone Number", extra_tags="phoneno1")
            duplicate_entry = True
        if m1Data['discord_ID']==leaderData['discord_ID']:
            messages.error(request, "Member 1 Discord ID is same as Leader Discord ID", extra_tags="discord_ID1")
            duplicate_entry = True
        if duplicate_entry:
            return redirect("/members-register")
        
        m2present = request.POST["m2Name"]!="" and request.POST["m2Email"]!="" and request.POST["m2Discord"]!="" and request.POST["m2RollNo"]!="" and request.POST["m2PhoneNo"]!=""
                    
        if m2present:
            #validating member2 details if present
            m2Data = {
                'name': request.POST["m2Name"],
                'email': request.POST["m2Email"],
                'rollno': request.POST["m2RollNo"],
                'phoneno': request.POST["m2PhoneNo"],
                'discord_ID': request.POST["m2Discord"],
            }
            m2Form = ParticipantForm(m2Data)
            if not m2Form.is_valid():
                for key in m2Form.errors:
                    messages.error(request, strip_tags(m2Form.errors[key]), extra_tags=f"{key}2")
                return redirect("/members-register")
            
            duplicate_entry = False
            if m2Data['email']==leaderData['email']:
                messages.error(request, "Member 2 email is same as Leader email", extra_tags="email2")
                duplicate_entry = True
            if m2Data['rollno']==leaderData['rollno']:
                messages.error(request, "Member 2 Roll Number is same as Leader Roll Number", extra_tags="rollno2")
                duplicate_entry = True
            if m2Data['phoneno']==leaderData['phoneno']:
                messages.error(request, "Member 2 Phone Number is same as Leader Phone Number", extra_tags="phoneno2")
                duplicate_entry = True
            if m2Data['discord_ID']==leaderData['discord_ID']:
                messages.error(request, "Member 2 Discord ID is same as Leader Discord ID", extra_tags="discord_ID2")
                duplicate_entry = True
            if m2Data['email']==m1Data['email']:
                messages.error(request, "Member 2 email is same as Member 1 email", extra_tags="email2")
                duplicate_entry = True
            if m2Data['rollno']==m1Data['rollno']:
                messages.error(request, "Member 2 Roll Number is same as Member 1 Roll Number", extra_tags="rollno2")
                duplicate_entry = True
            if m2Data['phoneno']==m1Data['phoneno']:
                messages.error(request, "Member 2 Phone Number is same as Member 1 Phone Number", extra_tags="phoneno2")
                duplicate_entry = True
            if m2Data['discord_ID']==m1Data['discord_ID']:
                messages.error(request, "Member 2 Discord ID is same as Member 1 Discord ID", extra_tags="discord_ID2")
                duplicate_entry = True
            if duplicate_entry:
                return redirect("/members-register")

        request.session.flush()
        
        teamData['email'] = leaderData['email']
        team = TeamForm(teamData).save()   #save team
        
        leaderData['team'] = team
        ParticipantForm(leaderData).save()  #save leader
        
        m1Data['team'] = team
        ParticipantForm(m1Data).save()  #save member1

        if m2present:
            m2Data['team'] = team
            ParticipantForm(m2Data).save()  #save member2
        
        #TODO: Send mails
        # subject = "Thank you for registering!"
        # password={'OTP':password,'Team_Name': teamData['teamName']} #password dict to be passed to email template
        # html_message = render_to_string('registration/registrationsuccessful.html', password) #html rendered message
        # message = strip_tags(html_message) #incase html render fails
        # from_email = settings.EMAIL_HOST_USER
        # send_mail(subject, message, from_email, to_list, html_message=html_message, fail_silently=False)
        
        return HttpResponse("success")
    
    sessionData = request.session.get('team', False)
    if sessionData:
        if sessionData.get('teamData', False) and sessionData.get('leaderData', False):
            context = {}
            msgs = messages.get_messages(request)
            for msg in msgs:
                context[msg.tags.replace(" ", "_")] = str(msg)
            msgs.used = True
            return render(request, 'registration/membersRegister.html', context=context)
    
    return redirect("/team-register")

