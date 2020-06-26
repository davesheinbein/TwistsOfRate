# Generated by Django 3.0.7 on 2020-06-25 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_gamecomment_api_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsoleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=350)),
                ('date', models.DateField(auto_now=True)),
                ('api_id', models.IntegerField()),
                ('console', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Console')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
