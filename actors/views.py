from rest_framework.generics import ListCreateAPIView

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorListCreateView(ListCreateAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


