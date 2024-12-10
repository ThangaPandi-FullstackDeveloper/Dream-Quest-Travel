from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from.models import *
from .forms import RegisterForm
from .forms import Book
from .forms import BookForm
from .forms import Contact
from .forms import contactForm
from django.contrib import messages
# Create your views here.


def Main(request):

    data = Image.objects.all()
    return render(request,"main.html",{"data": data})

def group(request):
    winder = G_winder.objects.all()
    summer = G_summer.objects.all()
    data = G_reserved.objects.all()
    return render(request,"group.html",{"winder": winder,"summer": summer,"data": data})

def indian(request):
    return render(request,"indian.html")

def india(request):
    india = India.objects.all()
    return render(request,"india.html",{"india":india})

def north(request):
    north = North.objects.all()
    return render(request,"north.html",{"north":north})

def education(request):
    education = Education.objects.all()
    return render(request,"education.html",{"education":education})

def south(request):
    south = South.objects.all()
    return render(request,"south.html",{"south":south})

def east(request):
    east = East.objects.all()
    return render(request,"east.html",{"east":east})

def europe(request):
    europe = Europe.objects.all()
    return render(request,"europe.html",{"europe":europe})

def honeymoon(request):
    honeymoon = Honeymoon.objects.all()
    kerala = Kerala.objects.all()
    shimla = Shimla.objects.all()
    manali = Manali.objects.all()
    andaman = Andaman.objects.all()
    munnar = Munnar.objects.all()
    kodai = Kodai.objects.all()
    ooty =  Ooty.objects.all()
    paris = Paris.objects.all()
    italy = Italy.objects.all()
    tailand = Tailand.objects.all()
    australia = Australia.objects.all()
    return render(request,"honeymoon.html",{"honeymoon":honeymoon,"kerala":kerala,"shimla":shimla,"manali":manali,
                  "andaman":andaman,"munnar":munnar,"kodai":kodai,"ooty":ooty,"paris":paris,"italy":italy,"tailand":tailand,"australia":australia})


def register(request):
    return render(request,"Register.html")


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request,"login.html")
    else:
        return render(request,'login.html')



def logout_user(request):
    logout(request)
    return redirect('main')


def book(request):
    form =  Book.objects.all()
    return render(request,'book.html',{'form':form})

def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking Successfully")
            return redirect('book')
        else:
            return render(request,"book.html",{'form': form})
    else:
        form = BookForm()
        return render(request,'book.html',{'form': form})

def contact(request):
    form =  Contact.objects.all()
    return render(request,'contact.html',{'form':form})

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "submit Successfully")
            return redirect('main')
        else:
            return render(request,"main.html",{'form': form})
    else:
        form = contactForm()
        return render(request,'contact.html',{'form': form})


def description(request):
        Image=i_Image.objects.all().filter(status=0)
        return render(request,"description.html",{"Image":Image})


def description_view(request,plan):
   if (Image.objects.filter(plan=plan,status=0)):
        products=i_Image.objects.filter(Image__plan=plan)
        return render(request,"main.html",{"products":products})
   else:
       messages.warning(request,"no such details")
       return redirect("description")
