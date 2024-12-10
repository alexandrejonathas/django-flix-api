from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerializer
from core.permissions import DefaultGlobalPermission


class ActorListCreateView(ListCreateAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)


class ActorRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)