from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.



def home(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        context = {'courses': courses}
        return render(request,'app/home.html')
    else: 
        return render(request,'app/base.html')

def Allcourse(request):
        courses = Course.objects.all()
        return render(request,'app/AllCourses.html', {'courses': courses})
def CourseDetails(request):
    return render(request,'app/CourseDetails.html')

def MyCourse(request):
    courseorders = CourseOrder.objects.all()
    return render(request,'app/MyCourses.html', {'courseorders': courseorders})

def LoginForm(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: messages.info(request, 'user hoặc password không chính xác!')  
    context = {}
    return render(request, 'app/LoginForm.html', context)


def RegisterForm(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/RegisterForm.html', context)

@csrf_exempt
def register_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)

        # Tạo CourseOrder mới
        course_order = CourseOrder()
        course_order.save()
        
        return JsonResponse({'status': 'success', 'message': 'Thêm khóa học thành công'})

    return JsonResponse({'status': 'fail', 'message': 'Thêm khóa học không thành công'})