from django import forms
from .models import Team, Participant

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['teamName', 'password', 'email']

    def save(self, *args, **kwargs):
        member = super(TeamForm, self).save(*args, **kwargs)
        member.set_password(self.cleaned_data["password"])
        member.save()
        return member

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'roll_no', 'phone_no','discord_ID', 'team']