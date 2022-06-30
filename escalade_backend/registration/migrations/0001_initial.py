# Generated by Django 4.0.2 on 2022-06-28 07:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=100, unique=True)),
                ('points', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('board', models.IntegerField(default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Invalid email address', regex='^[A-Za-z0-9._~+-]+@thapar\\.edu$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=9, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Invalid email address', regex='^[A-Za-z0-9._~+-]+@thapar\\.edu$')])),
                ('discord_ID', models.CharField(default='', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Enter a valid discord ID', regex='^.{2,32}#[0-9]{4}$')])),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]