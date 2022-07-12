from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    data = {'name': 'Cristina'}
    return render(request, 'home.html', data)

def fill_form(request):
    return render(request, 'form.html')

def student_list(request):

    if request.POST:
        print(request.POST)

        ns_name = request.POST.get('name') 
        ns_course = request.POST.get('course')
        ns_email = request.POST.get('email')

        new_student = Student(name = ns_name, course = ns_course, email = ns_email)
        new_student.save()

        # Grab all data for display
        students = Student.objects.all()
        data = {'students': students}

        return render(request, 'student_list.html', data)
