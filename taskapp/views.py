from django.shortcuts import render,redirect
from django.contrib import messages
from .models import person,blog

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if person.objects.filter(username=username,password=password).exists():
            obj = person.objects.get(username=username,password=password)
            return render(request,'index.html',{'obj':obj})
        else:
            messages.info('Invalid credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        address = request.POST['address']
        f=request.POST['fname']
        l=request.POST['lname']
        user_type=request.POST['user']
        
        if password1 == password2:
            if person.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif person.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = person.objects.create(user=user_type,firstname=f,lastname=l,username=username, email=email, password=password1,address=address)
                return redirect('login')
        else:
            messages.info(request,'Wrong passwords')
            return redirect('register')
    else:
        return render(request,'register.html')

def blogs(request):
    posts = blog.objects.all()
    return render(request, 'blogs.html',{'posts':posts})

def write1(request):
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        blogpost = blog.objects.create(title=title, body=body)  
        blogpost.save()
        return redirect('login')        
    else:
        return render(request,'write.html')
    
def post(request,pk):
    posts = blog.objects.get(id=pk)
    return render(request,'post.html',{'posts':posts})

def list(request):
    doctors = person.objects.all()
    return render(request, 'doctors.html',{'doctors':doctors})

def book(request):
    if request.method == "POST":
        doctor = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        return render(request,'details.html',{'doctor':doctor, 'date':date , 'time':time})
    else:
        return render(request,'book.html')
