from django.shortcuts import render,redirect,get_object_or_404
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info,warning
from .models import University,Universities_Course,Student,Lecutures
from accounts.models import Accounts

def university_apply(request):
    universities=Universities_Course.objects.all()
    return render(request,'university_apply.html',{'universities':universities})

def login_message(request):
    warning(request,"To enroll university courses login required.")
    return redirect('/')

@login_required(login_url='/unversity_apply/login_warn/')
def payment(request,course_id=None):
    course=Universities_Course.objects.get(id=course_id)
    return render(request,'payment.html',{'course':course})

def proceed_payment(request):
    email=request.user
    course=Universities_Course.objects.get(id=request.GET['course_id'])
    user=get_object_or_404(Accounts,email=email)
    student=Student.objects.filter(student=user,course_enroll=course)
    if student:
        info(request,"you already registered for this course.")
        return redirect(university_apply)
    else:
        Student.objects.create(student=user,course_enroll=course,paid=True)
    return redirect('/')

def display_lecture(request,uni_course):
    lectures=Lecutures.objects.all().filter(university_course=uni_course)
    return render(request,'university_lecture.html',{'lectures':lectures})




def lecture_play(request,lec_id=None):
    lecture = Lecutures.objects.get(id=lec_id)
    lecture_list=Lecutures.objects.all().filter(university_course=lecture.university_course).exclude(id=lec_id)
    return render(request,'lecture_play.html',{'lecture':lecture, 'lec_list':lecture_list})


