import random
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth

from .models import BoardLadder, BoardSnake, Question
from registration.models import Team


# Create your views here.
def login(request):
    if request.method == 'POST':
        TeamName = request.POST['TeamName']
        password=request.POST['password']

        team = auth.authenticate(teamName=TeamName, password=password)
        
        if team is not None :
            auth.login(request, team)
            print("logged in successfully")
            return redirect('/play')
        
        else:
            messages.info(request, "Invalid Credentials")
            print("lmao")
            return redirect('/login')
    return render(request, 'game/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')

def getRandomQuestion(team):
    level = 1 if team.position<=20 else 2 if team.position<=40 else 3 if team.position<=60 else 4
    ques_str = team.level1 if level==1 else team.level2 if level==2 else team.level3 if level==3 else team.level4
    if len(ques_str)==0:
        ques_bank = Question.objects.filter(level=level)
        ques = random.choice(ques_bank)
        return ques
    if level==1:
        idx = random.randrange(0, len(team.level1), 2)
        ques_id = team.level1[idx: idx+2]
        team.level1 = ques_str.replace(ques_id, '')
    elif level==2:
        idx = random.randrange(0, len(team.level2), 2)
        ques_id = team.level2[idx: idx+2]
        team.level2 = ques_str.replace(ques_id, '')
    elif level==3:
        idx = random.randrange(0, len(team.level3), 2)
        ques_id = team.level3[idx: idx+2]
        team.level3 = ques_str.replace(ques_id, '')
    else:
        idx = random.randrange(0, len(team.level4), 2)
        ques_id = team.level4[idx: idx+2]
        team.level4 = ques_str.replace(ques_id, '')
    print(ques_id)
    ques_id = int(ques_id)%5
    if ques_id==0:
        ques_id = 5
    ques = Question.objects.get(id=ques_id)
    return ques

@login_required(login_url="/login")
def play(request):
    team = request.user
    if request.method=="POST":
        answer = request.POST.get("answer")
        if answer!=team.current_ques.ans:
            return render(request, "game/start.html", context={
                "wrongAnswer": "true"
            })
        team.points += 10;
        team.position += team.dice_value
        team.dice_value = random.randint(1, 6)
        team.current_ques = getRandomQuestion(team)
        snakePresent = None
        ladderPresent = None
        snake = BoardSnake.objects.filter(boardNo=team.board, snakeHead=team.position).first()
        if snake is not None:
            snakePresent = "yes"
            team.position = snake.snakeTail
        else:
            ladder = BoardLadder.objects.filter(boardNo=team.board, ladderBottom=team.position).first()
            if ladder is not None:
                ladderPresent = "yes"
                team.position = ladder.ladderTop
        team.save()
        print(snakePresent, ladderPresent)
        return render(request, 'game/start.html', context={
            'correctAnswer': 'true',
            'snake': snakePresent,
            'ladder': ladderPresent
        })
    if team.current_ques==None:
        team.current_ques = getRandomQuestion(team)
        team.dice_value = random.randint(1, 6)
        team.save()
        print(team.level1)
    return render(request, 'game/start.html')

@require_http_methods(['POST'])
@login_required(login_url="/login")
def hint(request):
    team = request.user
    hint = None
    if team.points>=10:
        hint = team.current_ques.hint
        team.points -= 10
        team.save()
    return JsonResponse({
        'hint': hint
    })

@require_http_methods(["POST"])
@login_required(login_url="/login")
def sneakPeak(request):
    team = request.user
    if team.points<25:
        return JsonResponse()
    team.points -= 25
    nextPos = team.position + team.dice_value
    ladder = False
    snake = BoardSnake.objects.filter(snakeHead=nextPos).exists()
    if not snake:
        ladder = BoardLadder.objects.filter(ladderBottom=nextPos).exists()
    value = "snake" if snake else "ladder" if ladder else "none"
    return JsonResponse({
        'value': value
    })

@require_http_methods(["POST"])
@login_required(login_url='/login')
def reRoll(request):
    team = request.user
    if team.points<15:
        return JsonResponse({
            'value': None
        })
    team.points -= 15
    prevVal = team.dice_value
    value = random.randint(1, 6)
    while value==prevVal:
        value = random.randint(1, 6)
    team.dice_value = value
    team.save()
    return JsonResponse({
        'value': value
    })

@login_required(login_url='/login')
def getHead(request):
    if request.method=="POST":
        return render(request, "game/gethead.html", context={
            'color': 'blue'
        })
    if request.method=="HEAD":
        req = HttpResponse("")
        req['flag'] = "answer"
        return req
    return render(request, "game/getHead.html", context={
        'color': 'red'
    })
    
# @login_required(login_url='/login')
def leaderboard(request):
    top5=Team.objects.all().values('teamName','position').order_by('-position')[:5]
    # print(list(top5))
    # team1={
    #     'teamName': top5[0]['teamName'],
    #     'position': top5[0]['position']
    # }
    # team2={
    #     'teamName': top5[1]['teamName'],
    #     'position': top5[1]['position']
    # }
    # team3={
    #     'teamName': top5[2]['teamName'],
    #     'position': top5[2]['position']
    # }
    # team4={
    #     'teamName': top5[3]['teamName'],
    #     'position': top5[3]['position']
    # }
    # team5={
    #     'teamName': top5[4]['teamName'],
    #     'position': top5[4]['position']
    # }
   
    return render(request, "game/lead.html",context={'teams':list(top5)})
    # return render(request, "game/lead.html",context={
    #     'team1': team1,
    #     'team2': team2,
    #     'team3': team3,
    #     'team4': team4,
    #     'team5': team5,
    #     'teams':list(top5)
    # })
    
@login_required(login_url='/login')
def start(request):
    return render(request, "game/start.html")
