# Generated by Django 3.2.11 on 2022-10-06 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, help_text='Tell us a bit about yourself', max_length=1500, verbose_name='About')),
                ('is_seeking_job', models.BooleanField(default=False, help_text='Are you looking for employment?', verbose_name='Seeking employment')),
                ('is_working', models.BooleanField(default=False, help_text='Are you employed currently?', verbose_name='Currently employed?')),
                ('employer', models.CharField(blank=True, help_text='(If currently employed)', max_length=150, null=True, verbose_name='Your employer')),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('country_residence', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('mobile_number', models.CharField(blank=True, help_text='(eg: +97150XXXXXXX)', max_length=100, null=True, verbose_name='Your mobile number')),
                ('github', models.CharField(blank=True, help_text='https://github.com/Coders-HQ', max_length=100, null=True, verbose_name='Github account')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]