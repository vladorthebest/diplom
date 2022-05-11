from django.shortcuts import render
import sqlite3
from .models import lesson, name_group, lesson_e
import datetime
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
import django.views.generic 
from .etalon import etalon
from .classroom import classroom
from .par import parse
from django.http import HttpResponse
from .forms import lessonForm, lessoneForm


class LessonDetailView(DetailView, UpdateView):
    model = lesson
    template_name = 'mainapp/lesson.html'
    context_object_name = 'lesson'
    form_class = lessonForm
    success_url = '/day'

class EtalonDetailView(DetailView, UpdateView):
    model = lesson_e
    template_name = 'mainapp/lesson.html'
    context_object_name = 'lesson'
    form_class = lessoneForm
    success_url = '/etalon'

def main_e(request):
    lessons = lesson_e.objects.all()
    return render(request, 'mainapp/lessonse.html', {'lessons': lessons})

def main(request):
    d1 = datetime.datetime.today()
    d1 = d1 + datetime.timedelta(days=1)
    day = str(d1.isoweekday())
    print(day)
    if day == '6':
        d1 = d1 + datetime.timedelta(days=2)
    if day == '7':
        d1 = d1 + datetime.timedelta(days=1)

    date = str(d1.day) + '.' + str(d1.month) + '.' + str(d1.year)
    
    print(date)
    lessons = lesson.objects.filter(data=date)
    return render(request, 'mainapp/lessons.html', {'lessons': lessons})


def new_etalon(request):
    t = etalon()
    t.main()
    return render(request, 'mainapp/main_list.html')

def new_day(request):
    t = parse()
    t.parse_main()
    return render(request, 'mainapp/main_list.html')

def classroom_create(request):
    t = classroom()
    t.classroom_train_main()
    t.classroom_main()
    
    return render(request, 'mainapp/main_list.html')


def main_list(request):
    return render(request, 'mainapp/main_list.html')

def info(request):
    return render(request, 'mainapp/info.html')