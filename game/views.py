import random
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth

from .models import Booster, Opposer, Question
from registration.models import Team

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("/start")
    if request.method == 'POST':
        TeamName = request.POST['TeamName']
        password=request.POST['password']

        team = auth.authenticate(teamName=TeamName, password=password)
        
        if team is not None :
            # if team.is_loggedin:
            #     messages.error(request, "Already logged in from other browser!")
            #     return redirect('/login')
            auth.login(request, team)
            # team.is_loggedin = True
            # team.save()
            return redirect('/start')
        
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login')
    return render(request, 'game/login.html')

def logout(request):
    if request.user.is_anonymous:
        return redirect('/login')
    team = request.user
    # team.is_loggedin = False
    # team.save()
    auth.logout(request)
    return redirect('/login')

def getRandomQuestion(team, prev_ques_id):
    level = 1 if team.position<16 else 2 if team.position<33 else 3 if team.position<57 else 4
    ques_lst = team.level1 if level==1 else team.level2 if level==2 else team.level3 if level==3 else team.level4
    if len(ques_lst)==0:
        ques_bank = Question.objects.filter(level=level)
        ques = random.choice(ques_bank)
        while ques.id==prev_ques_id:
            ques = random.choice(ques_bank)
        return ques
    
    ques_id = random.choice(ques_lst)
    ques_lst.remove(ques_id)
    if level==1:
        team.level1 = ques_lst
    elif level==2:
        team.level2 = ques_lst
    elif level==3:
        team.level3 = ques_lst
    else:
        team.level4 = ques_lst
    ques = Question.objects.get(id=ques_id)
    return ques

@never_cache
@login_required(login_url="/login")
def play(request):
    team = request.user
    if team.position>80:
        return render(request, "game/game_over.html")
    if request.method=="POST":
        answer = request.POST.get("answer")
        if team.current_ques==None:
            return redirect('/play')
        if answer!=team.current_ques.ans:
            messages.error(request, "wrongAnswer", 'wrong')
            return redirect('/play')
        ques_lst = team.level1 if team.position<16 else team.level2 if team.position<33 else team.level3 if team.position<57 else team.level4
        if len(ques_lst):
            team.points += 10
        team.position += team.dice_value
        if team.position>80:
            team.position = 81
            team.dice_value = None
            team.current_ques = None
            team.hint_taken = False
            team.sneakpeek_taken = None
            team.save()
            return redirect("/play")
        beforeLocation = team.position
        opposerPresent = False
        boosterPresent = False
        opposer = Opposer.objects.filter(boardNo=team.board, start=team.position).first()
        if opposer is not None:
            opposerPresent = True
            team.position = opposer.end
        else:
            booster = Booster.objects.filter(boardNo=team.board, start=team.position).first()
            if booster is not None:
                boosterPresent = True
                team.position = booster.end
        team.dice_value = random.randint(1, 6)
        prev_ques_id = team.current_ques.id
        team.current_ques = getRandomQuestion(team, prev_ques_id)
        team.hint_taken = False
        team.sneakpeek_taken = None
        team.save()
        messages.success(request, "correctAnswer", 'correct')
        if opposerPresent:
            messages.info(request, "opposerPresent", 'opposer')
        if boosterPresent:
            messages.info(request, "opposerPresent", 'booster')
        messages.info(request, f"{beforeLocation}", 'before_location')
        return redirect('/play')
    context = {}
    if team.current_ques==None:
        team.current_ques = getRandomQuestion(team, -1)
        team.dice_value = random.randint(1, 6)
        team.hint_taken = False
        team.sneakpeek_taken = None
        team.save()
    else:
        msgs = messages.get_messages(request)
        for msg in msgs:
            if msg.tags=='correct success':
                context['correctAnswer'] = True
            elif msg.tags=='opposer info':
                context['opposer'] = True
            elif msg.tags=='booster info':
                context['booster'] = True
            elif msg.tags=='before_location info':
                context['beforeLocation'] = str(msg)
            elif msg.tags=='wrong error':
                context['wrongAnswer'] = True
        msgs.used = True
    return render(request, 'game/test.html', context=context)

@never_cache
@require_http_methods(['POST'])
@login_required(login_url="/login")
def hint(request):
    team = request.user
    hint = ''
    if team.hint_taken:
        hint = team.current_ques.hint
    elif team.points>=10:
        hint = team.current_ques.hint
        team.points -= 10
        team.hint_taken = True
        team.save()
    return JsonResponse({
        'value': hint,
        'points': team.points
    })

@never_cache
@require_http_methods(["POST"])
@login_required(login_url="/login")
def sneakPeek(request):
    team = request.user
    value = ""
    if team.sneakpeek_taken is not None:
        value = team.sneakpeek_taken
    elif team.points>=25:
        team.points -= 25
        nextPos = team.position + team.dice_value
        booster = False
        opposer = Opposer.objects.filter(boardNo=team.board, start=nextPos).exists()
        if not opposer:
            booster = Booster.objects.filter(boardNo=team.board, start=nextPos).exists()
        value = "opposer" if opposer else "booster" if booster else "none"
        team.sneakpeek_taken = value
        team.save()
    return JsonResponse({
        'value': value,
        'points': team.points
    })

@never_cache
@require_http_methods(["POST"])
@login_required(login_url='/login')
def reRoll(request):
    team = request.user
    if team.points>=15:
        team.points -= 15
        prevVal = team.dice_value
        value = random.randint(1, 6)
        while value==prevVal:
            value = random.randint(1, 6)
        team.dice_value = value
        team.sneakpeek_taken = None
        team.save()
    return JsonResponse({
        'value': team.dice_value,
        'points': team.points
    })

# @login_required(login_url='/login')
def leaderboard(request):
    top5=Team.objects.all().values('teamName','position').order_by('-position', '-points')[:5]
    
    team1={
        'teamName': top5[0]['teamName'],
        'position': top5[0]['position']
    }
    team2={
        'teamName': top5[1]['teamName'],
        'position': top5[1]['position']
    }
    team3={
        'teamName': top5[2]['teamName'],
        'position': top5[2]['position']
    }
    team4={
        'teamName': top5[3]['teamName'],
        'position': top5[3]['position']
    }
    team5={
        'teamName': top5[4]['teamName'],
        'position': top5[4]['position']
    }
   
    return render(request, "game/scoreboard.html",context={
        'team1': team1,
        'team2': team2,
        'team3': team3,
        'team4': team4,
        'team5': team5,
        'teams':list(top5)
    })
    
@login_required(login_url='/login')
def start(request):
    return render(request, "game/start.html")

def rulebook(request):
    return render(request, "game/rulebook.html")
