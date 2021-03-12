from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from hiretuber.models import Hiretuber
from youtubers.models import Youtuber
from webpages.models import Socialmedia
# Create your views here.

def login_user(request):
    s = Socialmedia.objects.get(id=1)
    data = {

        's': s,

    }
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are logged in ')
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid credential')
            return redirect('login_user')
    return render(request,'accounts/login_user.html',data)

def register(request):
    s = Socialmedia.objects.get(id=1)
    data = {

        's': s,

    }
    if request.method=='POST':
        firstname= request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login_user')



        else:
            messages.warning(request,'Password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html',data)


def logout_user(request):
    s = Socialmedia.objects.get(id=1)
    data = {

        's': s,

    }

    logout(request)
    return render(request,'accounts/logout_user.html',data)


@login_required(login_url='login_user')
def dashboard(request):
    s = Socialmedia.objects.get(id=1)
    h=Hiretuber.objects.filter(email=request.user.email)

    l=[]
    for i in h:
        l.append(i.tuber_id)


    k=[]
    for i in l:
        u=Youtuber.objects.get(id=i)
        k.append(u)



    data = {
        'k':k,
        's':s,

    }

    return render(request,'accounts/dashboard.html',data)