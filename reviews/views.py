from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(ListCreateAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    
