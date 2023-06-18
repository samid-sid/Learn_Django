from django import template
from django.template.loader import get_template
register = template.Library()

def my_template(value,arg):
    if arg == 'change':
        value = 'Mahdin'
        return value
    
    if arg == 'title':
        return value.title()
    
    
def show_courses():
    data = [
        {'id':1,'course':'C','Teacher':'Rayhan'},
        {'id':2,'course':'C++','Teacher':'Samid'},
        {'id':3,'course':'C#','Teacher':'Sara'},
    ]
    return {'courses':data}
    
# registar.filter('modify', my_template)
course_template = get_template('data/course.html')
register.filter('change_name',my_template)
register.inclusion_tag(course_template)(show_courses)