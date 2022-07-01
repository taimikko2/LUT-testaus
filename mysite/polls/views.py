from django.http import HttpResponse


def index(request):
    return HttpResponse("Moro siellä. Tämä on polls index.")

