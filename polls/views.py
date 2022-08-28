from django.http import HttpResponse


def index(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)

def results(request, question_id):

