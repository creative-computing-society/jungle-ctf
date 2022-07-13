from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import random
import string

from base64 import b64decode, b64encode

# Create your views here.

@login_required(login_url='/login')
def cookies(request):
    context = {}
    list = ['Steel Pan','Fiddle','Bamboo Flute','Bagpipes','Recorder','Wooden Flute','Viola','Harmonica','Spoons','Bass Guitar','table','thermometer','mirror','soap','bag','sandal','pencil','shovel','teddies','cookie jar','chalk','toothbrush']
    context['inputText'] = request.GET.get('input')
    context['outputText'] = random.choice(list)
    cookie = request.COOKIES.get('cookie', -1)
    if cookie=='18':
        context['image'] = 'webescques/img/0r3o5_c00k135.jpg' #answer
        context['inputText'] = 'Favourite Cookie'
        context['outputText'] = 'This image'
    else:
        context['image'] = 'webescques/img/cookies_trade.jpg'
    response = render(request, 'webescques/cookies.html', context=context)
    response.set_cookie('cookie', -1)
    return response

@login_required(login_url='/login')
def encryptCookies(request):
    context = {}
    cookie = request.COOKIES.get('auth')
    if cookie is not None:
        cookie = cookie.encode('utf-8')
        try:
            raw = b64decode(cookie)
            raw = raw.decode('utf-8')
            if raw=='JustA1Admin':
                context['flag'] = 'gather_story_bend' #answer
        except:
            messages.error(request, "Cannot decode cookie!")
    txt = b'JustA0Admin'
    encrypted = b64encode(txt)
    encrypted = str(encrypted, 'utf-8')
    response = render(request, 'webescques/encrypt_cookies.html', context=context)
    response.set_cookie('auth', encrypted)
    response.set_cookie('cookie', -1)
    return response

@login_required(login_url='/login')
def securePortal(request):
    key = request.GET.get("key")
    if key=='magnet_power_warm_ocean_its_sigh_till_end':
        response = render(request, 'webescques/securePortal.html')
        response['flag'] = 'pitch_class_factory' #answer
        return response
    return render(request, 'webescques/securePortalLogin.html')

@login_required(login_url='/login')
def basicInspect(request):
    return render(request, 'webescques/basicInspect.html', {
        'flag': 'front_dream_flow' #answer
    })

@login_required(login_url='/login')
def powerCookies(request):
    cookie = request.COOKIES.get('isAdmin')
    if cookie=='1':
        return render(request, "webescques/powerCookie.html", context={
            'flag': 'larger_butter_away' #answer
        })
    response = render(request, 'webescques/powerCookie.html', context={
        'cookie': cookie
    })
    response.set_cookie('isAdmin', 0, max_age=None)
    return response

@login_required(login_url='/login')
def ccsBrowserOptionsRequest(request):
    context={}
    user_agent = request.META['HTTP_USER_AGENT']
    if user_agent=='ccsbrowser':
        if request.method=='POST':
            context['postText'] = "It seems, however, to have had some importance as a post station."
        elif request.method=="GET":
            context['getText'] = "Things would get better."
        response = render(request, 'webescques/optionsRequest.html', context = context)
        if request.method=='OPTIONS':
            response['flag'] = "excitement_back_black" #answer
        else:
            response['flag'] = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        return response
    messages.error(request, f"You are not using ccsbrowser.")
    return render(request, 'webescques/ccsBrowser.html', context={
        'user_agent': user_agent
    })
