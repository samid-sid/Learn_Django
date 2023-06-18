from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime, timedelta
# Create your views here.


def Home(request):
    resposne = render(request, './book/base.html')
    resposne.set_cookie(
        'Name', 'Samid', expires=datetime.utcnow()+timedelta(7))
    return resposne


def set_session(request):
    data = {
        'name': 'samid',
        'age': 23,
        'lang': 'bangla'
    }
    request.session.update(data)

    return render(request, './book/base.html')


def get_session(request):
    data = request.session
    return render(request, './book/home.html', {'data': data})


def get_cookie(request):
    name = request.COOKIES.get('Name')
    return render(request, './book/home.html', {'Name': name})


def del_session(request):
    request.session.flush()
    return render(request,'./book/home.html')
    