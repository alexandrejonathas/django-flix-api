from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre

import json


@csrf_exempt
def genres_view(request, genre_id=None):

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


@csrf_exempt
def genres_find_update_delete(request, genre_id):

    if request.method == 'GET':

        genre = Genre.objects.filter(id=genre_id).first()

        if not genre:
            return HttpResponse(status=404)
        
        return JsonResponse(data={'id': genre.id, 'name': genre.name}, safe=False)
    
    if request.method == 'PUT':
        genre = Genre.objects.filter(id=genre_id).first()

        if not genre:
            return HttpResponse(status=404)
        
        data = json.loads(request.body.decode('utf-8'))

        genre.name = data['name']
        genre.save()

        return JsonResponse(data={'id': genre.id, 'name': genre.name}, safe=False)        

    if request.method == 'DELETE':
        genre = Genre.objects.filter(id=genre_id).first()

        if not genre:
            return HttpResponse(status=404)
        
        genre.delete()

        return HttpResponse(status=204)

    return HttpResponse(status=405)