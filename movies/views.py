from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateView(ListCreateAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

class MovieRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)    
