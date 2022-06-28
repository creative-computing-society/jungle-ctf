from django.contrib import admin

from escalade_backend.registration.models import Participant, Team

# Register your models here.
admin.site.register(Team)
admin.site.register(Participant)