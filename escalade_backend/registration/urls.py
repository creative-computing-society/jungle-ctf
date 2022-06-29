from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('team-register/', views.teamRegister, name="teamRegister"),
    path('members-register/', views.membersRegister, name="membersRegister"),
    path('delete-expired-sessions/', views.deleteExpiredSession, name="del"),
]