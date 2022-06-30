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
            context = {
                'teamName_error': "Team name taken"
            }
            return render(request, 'registration/teamRegister.html', context=context)

        leaderData = {
            'name': request.POST["leaderName"],
            'email': request.POST["leaderEmail"],
            'rollno': request.POST["leaderRollNo"],
            'phoneno': request.POST["leaderPhoneNo"],
            'discord_ID': request.POST["leaderDiscord"],
        }
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            context = {}
            for key in leaderForm.errors:
                context[f"{key}_error"] = strip_tags(leaderForm.errors[key])
            return render(request, 'registration/teamRegister.html', context=context)
        
        request.session['team'] = {
            'teamData': teamData,
            'leaderData': leaderData
        }
        request.session.set_expiry(3600)

        return redirect('/members-register')

    if request.session.get('team', False):
        del request.session['team']
    
    return render(request, 'registration/teamRegister.html')


def membersRegister(request):
    
    if request.method=='POST':
        teamData = request.session['team']['teamData']
        leaderData = request.session['team']['leaderData']

        context = {}

        form = TeamForm(teamData)
        if not form.is_valid():
            context['teamName_error'] = "Team name taken"
            return render(request, 'registration/teamRegister.html', context=context)
        
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            for key in leaderForm.errors:
                context[f"{key}_error"] = strip_tags(leaderForm.errors[key])
            return render(request, 'registration/teamRegister.html', context=context)

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
                context[f"{key}1_error"] = strip_tags(m1Form.errors[key])
            return render(request, 'registration/membersRegister.html', context=context)
        
        duplicate_entry = False
        
        if m1Data['email']==leaderData['email']:
            context["email1_error"] = "Member 1 email is same as Leader email"
            duplicate_entry = True
        
        if m1Data['rollno']==leaderData['rollno']:
            context["rollno1_error"] = "Member 1 Roll Number is same as Leader Roll Number"
            duplicate_entry = True
        
        if m1Data['phoneno']==leaderData['phoneno']:
            context["phoneno1_error"] = "Member 1 Phone Number is same as Leader Phone Number"
            duplicate_entry = True
        
        if m1Data['discord_ID']==leaderData['discord_ID']:
            context["discord_ID1_error"] = "Member 1 Discord ID is same as Leader Discord ID"
            duplicate_entry = True
        
        if duplicate_entry:
            return render(request, 'registration/membersRegister.html', context=context)
        
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
                    context[f"{key}2_error"] = strip_tags(m2Form.errors[key])
                return render(request, 'registration/membersRegister.html', context=context)
            
            #checking duplicate entries
            duplicate_entry = False
            
            if m2Data['email']==leaderData['email']:
                context["email2_error"] = "Member 2 email is same as Leader email"
                duplicate_entry = True
            
            if m2Data['rollno']==leaderData['rollno']:
                context["rollno2_error"] = "Member 2 Roll Number is same as Leader Roll Number"
                duplicate_entry = True
            
            if m2Data['phoneno']==leaderData['phoneno']:
                context["phoneno2_error"] = "Member 2 Phone Number is same as Leader Phone Number"
                duplicate_entry = True
            
            if m2Data['discord_ID']==leaderData['discord_ID']:
                context["discord_ID2_error"] = "Member 2 Discord ID is same as Leader Discord ID"
                duplicate_entry = True
            
            if m2Data['email']==m1Data['email']:
                context["email2_error"] = "Member 2 email is same as Member 1 email"
                duplicate_entry = True
            
            if m2Data['rollno']==m1Data['rollno']:
                context["rollno2_error"] = "Member 2 Roll Number is same as Member 1 Roll Number"
                duplicate_entry = True
            
            if m2Data['phoneno']==m1Data['phoneno']:
                context["phoneno2_error"] = "Member 2 Phone Number is same as Member 1 Phone Number"
                duplicate_entry = True
            
            if m2Data['discord_ID']==m1Data['discord_ID']:
                context["discord_ID2_error"] = "Member 2 Discord ID is same as Member 1 Discord ID"
                duplicate_entry = True
            
            if duplicate_entry:
                return render(request, 'registration/membersRegister.html', context=context)

        request.session.flush()
        
        try:
            teamData['email'] = leaderData['email']
            team = TeamForm(teamData).save()   #save team
            
            leaderData['team'] = team
            ParticipantForm(leaderData).save()  #save leader
            
            m1Data['team'] = team
            ParticipantForm(m1Data).save()  #save member1

            if m2present:
                m2Data['team'] = team
                ParticipantForm(m2Data).save()  #save member2
        except:
            messages.error(request, "Something went wrong.")
        
        #TODO: Send mails
        subj = "Thank you for registering!"
        credentials={'OTP':teamData['password'],'Team_Name': teamData['teamName']} #password dict to be passed to email template
        html_message = render_to_string('registration/register.html', credentials) #html rendered message
        message = strip_tags(html_message) #incase html render fails
        from_email = settings.EMAIL_HOST_USER
        
        print(from_email)
        to_list=[leaderData['email']]
        
        send_mail(subj, message, from_email, to_list, html_message=html_message, fail_silently=False)
        
        messages.success(request, "Form filled successfully")
        return redirect("/team-register")
    
    sessionData = request.session.get('team', False)
    if sessionData:
        if sessionData.get('teamData', False) and sessionData.get('leaderData', False):
            return render(request, 'registration/membersRegister.html')
    
    return redirect("/team-register")

