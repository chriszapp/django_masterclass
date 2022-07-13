from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    data = {'name': 'Cristina', 'students': students}
    return render(request, 'home.html', data)

def fill_form(request):
    return render(request, 'form.html')

def student_list(request):
    if request.POST:
        print(request.POST)
    return render(request, 'form.html')
    