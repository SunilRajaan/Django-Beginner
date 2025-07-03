from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Sunil')

def about(request):
    return HttpResponse('About Sunil')
