# Generated by Django 5.1.3 on 2024-11-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_resume_alter_movie_actors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]
