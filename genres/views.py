from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreListCreateView(ListCreateAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)


class GenreRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)

