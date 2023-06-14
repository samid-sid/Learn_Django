from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Contact(request):
    return HttpResponse("""
                        <h1> This is Contact Page </h1>
                        <a href = "/first_app/about/"> About </a> <br>
                        <a href = "/second_app/feedback/"> Feedback </a> <br>
                        <a href = "/second_app/course/"> Course </a> <br>
                        """)

def About(request):
       return HttpResponse("""
                        <h1> This is About Page </h1>
                        <a href = "/first_app/contact/"> Contact </a> <br>
                        <a href = "/second_app/feedback/"> Feedback </a> <br>
                        <a href = "/second_app/course/"> Course </a> <br>
                        """)

