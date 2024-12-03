from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return 0