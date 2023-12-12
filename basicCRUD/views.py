from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request,'index.html', {"students": students})

def store(request):
    nis= request.POST['nis']
    name= request.POST['name']
    address= request.POST['address']
    birth_date= request.POST['birth_date']
    student = Student(nis=nis, name=name,address=address,birth_date=birth_date)

    student.save()

    return redirect(reverse('index'))

def show(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {"student": student})

def update(request, student_id):
    nis= request.POST['nis']
    name= request.POST['name']
    address= request.POST['address']
    birth_date= request.POST['birth_date']

    student = Student.objects.get(pk=student_id)
    student.nis = nis
    student.name = name
    student.address = address
    student.birth_date = birth_date

    student.save()

    return redirect(f'/students/{student_id}')

def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect(reverse('index'))