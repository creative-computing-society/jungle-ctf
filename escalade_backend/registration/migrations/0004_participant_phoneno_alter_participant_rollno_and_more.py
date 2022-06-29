# Generated by Django 4.0.2 on 2022-06-29 15:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_team_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='phoneno',
            field=models.CharField(default=0, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phoneno', message='Invalid Phone Number', regex='^[0-9]{10}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participant',
            name='rollno',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_rollno', message='Invalid Roll Number', regex='^[0-9]{9}$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='board',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
