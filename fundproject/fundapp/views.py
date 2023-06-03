from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import logout
from django.db.models import Q

def index(request):
    return render (request,'home.html')

def home(request):
    return render (request,"home.html")

def project(request):
    return render (request,"project.html")




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if the username is already taken
        if register.objects.filter(username=username).exists():
            error_message = 'Username is already taken.'
            return render(request, 'register.html', {'error_message': error_message})
        # Create a new user
        else:
            user = register.objects.create(username=username, password=password, email=email)
            user.save()

            return render(request,'login.html')  # Redirect to the login page after successful registration

    return render(request, 'register.html')

def projectlist(request):
    user_id = request.session.get("u_id")
    if not user_id:
        return redirect("login")
    try:
        user = register.objects.get(id=user_id)
    except register.DoesNotExist:
        return redirect("login")
    
    projects = Project.objects.all().order_by('-id') 
    context = {
        "user": user,
        "projects": projects
    }
    
    return render(request, "projectlist.html", context)


def base(request):
    return render(request,"base.html")

def login(request):
    if request.POST:
        email=request.POST.get("email")
        password=request.POST.get("password")
        log=register.objects.filter(email=email,password=password)
        if log:
            request.session['u_id']=log[0].id
            return redirect('/projectlist')
      
    else:       
        return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('/')

def contributions(request):
    uid=request.session['u_id']
    user=register.objects.get(id=uid)
    cont=Contribution.objects.filter(user=user)
    return render(request,'contrib.html',{'contributions':cont})

def donate(request,pk):
    uid=request.session['u_id']
    user=register.objects.get(id=uid)
    p=Project.objects.get(id=pk)
    if request.method == "POST":
        name=request.POST["uname"]
        amt=request.POST['amount']

        new=Contribution.objects.create(project=p,contributor_name=name,amount=amt,user=user)
        new.save()
        messages.success(request,f"{name} contributed {amt} out of {p.amount}"
                         )
        return render(request,'pay.html',{'n':new})
    
    else:
        context={'p':p,'u':user}
        return render(request,"donate.html",context)

def projectview(request):
    
    return render(request, 'projectviews.html')

def about(request):
    return render(request,'about.html')



def category(request):
    cat=Category.objects.all()
    return render(request,'category.html',{"cat":cat})

def projectshow(request):
    id=request.GET.get('id')
    show=Project.objects.filter(category_id=id)
    return render(request,"projectshow.html",{"show":show})

def searchproject(request):
    query=request.GET.get('query')
    projects=Project.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render (request,'search.html',{'query':query , 'projects':projects})

def pay(request):
    return render(request,'pay.html')
def contactus(request):
    return render(request,'contactus.html')

def payment(request):
    return render(request,'payment.html')

def money(request):
    return render(request,'money.html')



