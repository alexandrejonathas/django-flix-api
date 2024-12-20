# Generated by Django 5.1.3 on 2024-11-29 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actor_nationality'),
        ('genres', '0001_initial'),
        ('movies', '0002_alter_movie_actors_alter_movie_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='resume',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='actors.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre'),
        ),
    ]
