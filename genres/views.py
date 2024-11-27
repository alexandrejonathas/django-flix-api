from django.shortcuts import HttpResponse
from django.http import JsonResponse

from genres.models import Genre

import json

def genres_view(request):

    if request.method == 'GET':
        genres = Genre.objects.all()

        data = [{'id': genre.id, 'name': genre.name} for genre in genres]

        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        genre = Genre(name=data['name'])
        genre.save()

        return JsonResponse(data={'id': genre.id, 'name': genre.name}, status=201, safe=False)

    return HttpResponse(status=405)


