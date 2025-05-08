from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *


def hello_view(request):
    return HttpResponse(
        """
        <h1>Salom, bu HttpResponse orqali yuborildi!</h1>
        <hr>
        """
    )


def home_view(request):
    return render(request, 'index.html')


def students_view(request):
    students = Talaba.objects.all()

    search = request.GET.get('search')
    if search is not None:
        students = students.filter(ism__contains=search)

    context = {
        'students': students,
        'search': search,
    }
    return render(request, 'students.html', context)


def authors_view(request):
    authors = Muallif.objects.all()

    gender = request.GET.get('gender')
    if gender is not None and gender != 'all':
        authors = authors.filter(jins=gender)

    context = {
        'authors': authors,
        'genders': Muallif.JINS_CHOICES,
        'g': gender,
    }
    return render(request, 'authors.html', context)


def student_view(request, student_id):
    student = Talaba.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'student-details.html', context)


def reader_students_view(request):
    students = Talaba.objects.filter(kitob_soni__gt=0)
    context = {
        'students': students,
    }
    return render(request, 'reader-students.html', context)


def student_delete_view(request, student_id):
    student = Talaba.objects.get(id=student_id)
    student.delete()
    return redirect('students')


def author_delete_view(request, author_id):
    student = Muallif.objects.get(id=author_id)
    student.delete()
    return redirect('authors')


def author_delete_confirm_view(request, author_id):
    author = Muallif.objects.get(id=author_id)
    context = {
        'author': author,
    }
    return render(request, 'author-confirm-delete.html', context)
