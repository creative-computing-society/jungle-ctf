from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Participant, Team
from django.contrib.sessions.models import Session
from django.contrib.admin import AdminSite

AdminSite.site_header = "Escalade Administration"
AdminSite.site_title = "Escalade site admin"

# Register your models here.

##Team##
class TeamResource(resources.ModelResource):
    class Meta:
        model = Team
        exclude = ('id',)
        import_id_fields = ('uuid',)


class TeamAdmin(ImportExportModelAdmin):
    resource_class = TeamResource
    list_display = ('uuid','teamName', 'points', 'position', 'board', 'members', 'current_ques', 'solved_ques')
    list_display_links = ('uuid', 'teamName')
    # list_filter = ('position',)
    search_fields = ('uuid','teamName', 'position')
    list_per_page = 25
    def members(self, obj):
        return (obj.participant_set.count())
    def solved_ques(self, obj):
        return int(70-len(obj.level1)/2-len(obj.level2)/2-len(obj.level3)/2-len(obj.level4)/2)

admin.site.register(Team, TeamAdmin)

##Participant##
class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'roll_no', 'phone_no', 'email', 'discord_ID', 'team', 'team__teamName')

class ParticipantAdmin(ImportExportModelAdmin):
    resource_class = ParticipantResource
    list_display = ('id', 'name', 'email', 'roll_no', 'phone_no', 'team')
    list_display_links = ('id', 'name')
    # list_filter = ('team',)
    search_fields = ('name', 'email', 'roll_no', 'discord_ID', 'phone_no', 'team__teamName')
    list_per_page = 25

admin.site.register(Participant, ParticipantAdmin)

##Session##
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expire_date']

admin.site.register(Session, SessionAdmin)
