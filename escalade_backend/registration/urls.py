from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.teamRegister, name="register"),
    path('complete-register/', views.membersRegister, name="membersRegister"),
    path('delete-expired-sessions/', views.deleteExpiredSession, name="del"),
]