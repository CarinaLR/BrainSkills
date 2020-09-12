# Generated by Django 3.1 on 2020-09-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainSkills', '0002_auto_20200908_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.ManyToManyField(related_name='levels', to='brainSkills.Level'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='service',
        ),
        migrations.AddField(
            model_name='student',
            name='service',
            field=models.ManyToManyField(related_name='services', to='brainSkills.Service'),
        ),
    ]
