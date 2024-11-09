from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    teacher = request.user.teacher
    students = Student.objects.filter(teacher=teacher)
    return render(request, 'portal/home.html', {'students': students})

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.teacher = request.user.teacher  # Set the teacher
            student.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'portal/add_student.html', {'form': form})

