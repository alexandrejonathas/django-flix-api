# Generated by Django 5.1.3 on 2024-11-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actor_nationality'),
        ('movies', '0004_remove_movie_actors_movie_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='actors.actor'),
        ),
    ]
