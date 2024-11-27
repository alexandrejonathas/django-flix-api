from django.http import JsonResponse


def index(request):

    return JsonResponse(data={'id': '1', 'name': 'Genre mock'})
