from django.db import models


NATIONALITY_CHOICES = (
    ('ARG', 'Argentina'),
    ('BR', 'Brasil'),
    ('CRO', 'Croacia'),
    ('DIN', 'Dinamarca'),
    ('ESP', 'Espanha'),
    ('FRA', 'França'),
    ('GEO', 'Georgia'),
    ('HOL', 'Holanda'),
    ('ITA', 'Italia'),
    ('JAP', 'Japao'),
)


class Actor(models.Model):

    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=False)
    nationality = models.CharField(
        max_length=100, 
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
