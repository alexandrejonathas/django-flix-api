from django.shortcuts import HttpResponse
from django.http import JsonResponse

from genres.models import Genre

def list(request):

    if request.method == 'GET':
        genres = Genre.objects.all()

        data = [{'id': genre.id, 'name': genre.name} for genre in genres]

        return JsonResponse(data, safe=False)

    return HttpResponse(status_code=405)
