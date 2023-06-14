from django.http import HttpResponse


def Home(request):
    return HttpResponse("""
                        <h1> This is Home Page </h1>
                        <a href = "/first_app/about/"> About </a> <br>
                        <a href = "/first_app/contact/"> Contact </a> <br>
                        <a href = "/second_app/course/"> Course </a> <br>
                        <a href = "/second_app/feedback/"> Feedback </a> <br>
                        
                        """)