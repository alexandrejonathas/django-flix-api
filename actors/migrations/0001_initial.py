# Generated by Django 5.1.3 on 2024-11-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(null=True)),
                ('nationality', models.CharField(blank=True, choices=[('ARG', 'Argentina'), ('BR', 'Brasil'), ('CRO', 'Croacia'), ('DIN', 'Dinamarca'), ('ESP', 'Espanha'), ('FRA', 'França'), ('GEO', 'Georgia'), ('HOL', 'Holanda'), ('ITA', 'Italia'), ('JAP', 'Japao')], max_length=100, null=True)),
            ],
        ),
    ]
