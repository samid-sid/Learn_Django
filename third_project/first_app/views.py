from django.shortcuts import render

# Create your views here.
def Home(request):
    dic ={'name':'i am samid','marks': 88, 'lst': [4,5,2,6],
          'blog':"asdf gasdg gaasdg adsg sadg adsg saga g asdg gasgda asg asgasg asg"
    }
    return render(request,'./file/index.html',context=dic)