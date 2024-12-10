from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer
from core.permissions import DefaultGlobalPermission


class MovieListCreateView(ListCreateAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)

class MovieRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)    
