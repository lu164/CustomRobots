# Generated by Django 2.2.28 on 2022-10-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_alter_exercise_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='configuration',
            field=models.TextField(default="{}"),
        ),
    ]