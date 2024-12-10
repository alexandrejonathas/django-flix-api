from core.tests import BaseTest

from actors.models import Actor


class ActorBaseTest(BaseTest):

    def make_actor(self, name='Padrão', nationality=('USA', 'Estados Unidos')):
        return Actor.objects.create(name=name, nationality=nationality)