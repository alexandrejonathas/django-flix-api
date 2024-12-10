from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from core.permissions import DefaultGlobalPermission


class ReviewListCreateView(ListCreateAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)


class ReviewRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, DefaultGlobalPermission)    
