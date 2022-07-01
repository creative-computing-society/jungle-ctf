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
    context = {}
    msgs = messages.get_messages(request)
    if msgs:
        for msg in msgs:
            if str(msg)=="formError":
                context['msg'] = 'failed'
                context['error'] = 'error'
            elif str(msg)=="formSuccess":
                context['msg'] = 'success'
        msgs.used = True
    return render(request, "registration/index.html", context=context)

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
            return render(request, 'registration/form.html', context=context)

        leaderData = {
            'name': request.POST["leaderName"],
            'email': request.POST["leaderEmail"],
            'roll_no': request.POST["leaderRollNo"],
            'phone_no': request.POST["leaderPhoneNo"],
            'discord_ID': request.POST["leaderDiscord"],
        }
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            context = {}
            for key in leaderForm.errors:
                context[f"{key}_error"] = strip_tags(leaderForm.errors[key])
                print(strip_tags(leaderForm.errors[key]))
            return render(request, 'registration/form.html', context=context)
        
        request.session['team'] = {
            'teamData': teamData,
            'leaderData': leaderData
        }
        request.session.set_expiry(3600)

        return redirect('/complete-register')

    if request.session.get('team', False):
        del request.session['team']
    
    return render(request, 'registration/form.html')


def membersRegister(request):
    
    if request.method=='POST':
        teamData = request.session['team']['teamData']
        leaderData = request.session['team']['leaderData']

        context = {}

        form = TeamForm(teamData)
        if not form.is_valid():
            context['teamName_error'] = "Team name taken"
            return render(request, 'registration/form.html', context=context)
        
        leaderForm = ParticipantForm(leaderData)
        if not leaderForm.is_valid():
            for key in leaderForm.errors:
                context[f"{key}_error"] = strip_tags(leaderForm.errors[key])
            return render(request, 'registration/form.html', context=context)

        m1Data = {
            'name': request.POST["m1Name"],
            'email': request.POST["m1Email"],
            'roll_no': request.POST["m1RollNo"],
            'phone_no': request.POST["m1PhoneNo"],
            'discord_ID': request.POST["m1Discord"],
        }
        m1Form = ParticipantForm(m1Data)
        if not m1Form.is_valid():
            for key in m1Form.errors:
                context[f"{key}1_error"] = strip_tags(m1Form.errors[key])
            return render(request, 'registration/member.html', context=context)
        
        duplicate_entry = False
        
        if m1Data['email']==leaderData['email']:
            context["email1_error"] = "Participant with this email already exists."
            duplicate_entry = True
        
        if m1Data['roll_no']==leaderData['roll_no']:
            context["roll_no1_error"] = "Participant with this Roll no already exists."
            duplicate_entry = True
        
        if m1Data['phone_no']==leaderData['phone_no']:
            context["phone_no1_error"] = "Participant with this Phone no already exists."
            duplicate_entry = True
        
        if m1Data['discord_ID']==leaderData['discord_ID']:
            context["discord_ID1_error"] = "Participant with this Discord ID already exists."
            duplicate_entry = True
        
        if duplicate_entry:
            return render(request, 'registration/member.html', context=context)
        
        m2present = request.POST["m2Name"]!="" and request.POST["m2Email"]!="" and request.POST["m2Discord"]!="" and request.POST["m2RollNo"]!="" and request.POST["m2PhoneNo"]!=""
                    
        if m2present:
            #validating member2 details if present
            m2Data = {
                'name': request.POST["m2Name"],
                'email': request.POST["m2Email"],
                'roll_no': request.POST["m2RollNo"],
                'phone_no': request.POST["m2PhoneNo"],
                'discord_ID': request.POST["m2Discord"],
            }
            m2Form = ParticipantForm(m2Data)
            if not m2Form.is_valid():
                for key in m2Form.errors:
                    context[f"{key}2_error"] = strip_tags(m2Form.errors[key])
                return render(request, 'registration/member.html', context=context)
            
            #checking duplicate entries
            duplicate_entry = False
            
            if m2Data['email']==leaderData['email']:
                context["email2_error"] = "Participant with this email already exists."
                duplicate_entry = True
            
            if m2Data['roll_no']==leaderData['roll_no']:
                context["rollno2_error"] = "Participant with this Roll no already exists."
                duplicate_entry = True
            
            if m2Data['phone_no']==leaderData['phone_no']:
                context["phoneno2_error"] = "Participant with this Phone no already exists."
                duplicate_entry = True
            
            if m2Data['discord_ID']==leaderData['discord_ID']:
                context["discord_ID2_error"] = "Participant with this Discord ID already exists."
                duplicate_entry = True
            
            if m2Data['email']==m1Data['email']:
                context["email2_error"] = "Participant with this email already exists."
                duplicate_entry = True
            
            if m2Data['roll_no']==m1Data['roll_no']:
                context["rollno2_error"] = "Participant with this Roll no already exists."
                duplicate_entry = True
            
            if m2Data['phone_no']==m1Data['phone_no']:
                context["phoneno2_error"] = "Participant with this Phone no already exists."
                duplicate_entry = True
            
            if m2Data['discord_ID']==m1Data['discord_ID']:
                context["discord_ID2_error"] = "Participant with this Discord ID already exists."
                duplicate_entry = True
            
            if duplicate_entry:
                return render(request, 'registration/member.html', context=context)

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
            messages.error(request, "formError")
            return redirect('/')
        
        #TODO: add raw img source to <img src:> in register.html
        # subj = "Thank you for registering!"
        # credentials={'OTP':teamData['password'],'Team_Name': teamData['teamName']} #password dict to be passed to email template
        # html_message = render_to_string('registration/register.html', credentials) #html rendered message
        # message = strip_tags(html_message) #incase html render fails
        # from_email = settings.EMAIL_HOST_USER
        
        # print(from_email)
        # to_list=[leaderData['email']]
        
        # send_mail(subj, message, from_email, to_list, html_message=html_message, fail_silently=False)
        
        messages.success(request, "formSuccess")
        return redirect("/")
    
    sessionData = request.session.get('team', False)
    if sessionData:
        if sessionData.get('teamData', False) and sessionData.get('leaderData', False):
            return render(request, 'registration/member.html')
    
    return redirect("/register")

