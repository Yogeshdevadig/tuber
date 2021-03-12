from django.shortcuts import render,redirect
from .models import *
from youtubers.models import *

# Create your views here.

def home(request):
    slides = Slider.objects.all()
    team = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.order_by('-created_date')
    s = Socialmedia.objects.get(id=1)

    data={
        's':s,
        'slides':slides,
        'team':team,
        'featured_youtubers':featured_youtubers,
        'all_youtubers':all_youtubers,
    }
    return render(request,'webpages/home.html',data)

def about(request):
    s = Socialmedia.objects.get(id=1)
    team = Team.objects.all()
    data={
        's':s,
        'team':team
    }
    return render(request,'webpages/about.html',data)

def contact(request):
    s = Socialmedia.objects.get(id=1)
    data = {
        's': s
    }
    return render(request,'webpages/contact.html',data)

def services(request):
    s = Socialmedia.objects.get(id=1)
    data = {
        's': s
    }
    return render(request,'webpages/services.html',data)

def contactus(request):
    if request.method=='POST':
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name= request.POST['company_name']
        subject = request.POST['subject']
        details = request.POST['details']

        c = ContactUsForm(fullname=fullname,phone=phone,email=email,company_name=company_name,subject=subject,details=details)
        c.save()
    return redirect('home')