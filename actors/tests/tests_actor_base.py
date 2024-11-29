from django.test import TestCase

from actors.models import Actor


class ActorBaseTest(TestCase):

    def make_actor(self, name='Padrão', nationality=('USA', 'Estados Unidos')):
        return Actor.objects.create(name=name, nationality=nationality)