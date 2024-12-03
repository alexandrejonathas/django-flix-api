from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateView(ListCreateAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer    
