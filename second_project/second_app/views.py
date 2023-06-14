from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Course(request):
   return HttpResponse("""
                        <h1> This is Course Page </h1>
                        <a href = "/first_app/about/"> About </a> <br>
                        <a href = "/first_app/contact/"> Contact </a> <br>
                        <a href = "/second_app/feedback/"> feedback </a> <br>
                        """)

def Feedback(request):
   return HttpResponse("""
                        <h1> This is Feedback Page </h1>
                        <a href = "/first_app/about/"> About </a> <br>
                        <a href = "/first_app/contact/"> Contact </a> <br>
                        <a href = "/second_app/course/"> Course </a> <br>
                        """)