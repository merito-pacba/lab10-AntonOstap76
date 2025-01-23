from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Category
from .forms import JobForm


def loginPage(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('job-list')
        else:
            messages.error(request, 'Username or Password does not exist')

    context={'page':page}  
    
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username  = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during regestration')

    context={'form': form}
    return render ( request , 'base/login_register.html', context)



def home(request):
    context={}
    return render(request,'base/home.html')

def job(request, pk):
    job=Job.objects.get(id=pk)
    context={'job':job}
    return render(request, 'base/job.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    jobs = user.job_set.all()
    categories = Category.objects.all()
    context={'user':user,
             'jobs':jobs,
             'categories': categories}
    return render(request, 'base/profile.html',context)

def joblist(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    jobs = Job.objects.filter(
        Q(category__name__icontains=q)|
        Q(title__icontains=q)|
        Q(description__icontains=q)
    )
    categories = Category.objects.all()
    job_count = jobs.count()
    context={'jobs':jobs,
             'categories':categories,
             'job_count':job_count}
    return render(request, 'base/joblist.html', context)

@login_required(login_url='login')
def createJob(request):
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('job-list')

    context={'form': form}
    return render(request, 'base/job_form.html', context)
@login_required(login_url='login')
def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.user != job.created_by:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job-list')


    context={'form':form}
    return render(request, 'base/job_form.html', context)

@login_required(login_url='login')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)

    if request.user != job.created_by:
        return HttpResponse('You are not allowed here!!!')
    
    if request.method == 'POST':
        job.delete()
        return redirect ('job-list')
    return render(request, 'base/delete.html', {'obj':job})
