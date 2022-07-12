from django.urls import path, include
from . import views

urlpatterns = [
    path('trader/', views.cookies, name='cookies'),
    path('main-search/', views.encryptCookies, name='encryptCookies'),
    path('portal/', views.securePortal, name='securePortal'),
    path('chat/', views.basicInspect, name='basicInspect'),
    path('passbook/', views.powerCookies, name='powerCookies'),
    path('website/', views.ccsBrowserOptionsRequest, name='ccsBrowserOptionsRequest'),
]
