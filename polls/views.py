from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Suck it</h1>")