# Generated by Django 3.1 on 2020-09-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainSkills', '0003_auto_20200912_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='progress',
        ),
    ]