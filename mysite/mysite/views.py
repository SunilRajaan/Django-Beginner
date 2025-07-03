from django.http import HttpResponse
from django.shortcuts import render

"""
# code for video 1
def index(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=1&pp=iAQB"> Django CodeWithHarry</a>''')

def about(request):
    return HttpResponse('About Sunil')
"""

"""
# creating pipe line as well as add back function
def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first <a href='/'>back</a>")

def newlineremove(request):
    return HttpResponse("newlineremove <a href='/'>back</a>")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount <a href='/'>back</a>")
"""


# template
def index(request):
    params = {'name': 'Sunil', 'place': 'Nepal'}
    return render(request, 'index.html', params)





