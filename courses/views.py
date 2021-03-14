from django.shortcuts import render,redirect
from django.contrib.messages import warning
from django.contrib.auth.decorators import login_required
from .models import Channel_Details,Course_Type,Video_lecture

def courses(request):
    courses=Course_Type.objects.all()
    channels=Channel_Details.objects.all()
    return render(request,'courses.html',{'courses':courses,'channels':channels})

def login_message(request):
    warning(request,"To watch free courses login required.")
    return redirect('/')

@login_required(login_url='/courses/menu/login_warn/')
def show_course_by_chanel(request,channel_id=None,vid=None):
    if vid:
        video=Video_lecture.objects.get(vid=vid)
    else:
        video=None
    videos=Video_lecture.objects.filter(channel_name=channel_id).order_by('-uploaded_on')
    return render(request,'video_page.html',{'lectures':videos,'req_video':video})



