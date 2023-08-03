from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Event
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.


def register(request):
    obj=Event.objects.all()
    return render(request,'base_page/base_page.html',{'obj':obj})
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('E_name')
        category=request.POST.get('E_category')
        location=request.POST.get('E_location')
        sub_location=request.POST.get('S_loaction')
        date= request.POST.get('date')
        time=request.POST.get('E_time')
        e_type=request.POST.get('E_type')
        amount=request.POST.get('E_amount')
        desc=request.POST.get('E_disc')
        adress=request.POST.get('E_adress')
        link=request.POST.get('E_link')
        images=request.FILES.getlist('img')
        for image in images:
            a = Event(name=name, desc=desc, location=location, sub_location=sub_location, date=date, e_type=e_type, image=image,category=category,time=time,amount=amount,adress=adress,link=link)
            a.save()
        redirect('/')
        print("record is saved")
    return render(request,'base_page/add_event.html')



def search(request):
    query1=request.GET.get('q1')
    query2=request.GET.get('q2')
    query3=request.GET.get('q3')
    query4=request.GET.get('q4')
    events = Event.objects.all()
    if(query1):
        events = events.filter(name__contains=query1)
    if(query2):
        events = events.filter(location__contains=query2)
    if(query3):
        events = events.filter(sub_location__contains=query3)
    if(query4):
        events=events.filter(category__contains=query4)
    return render(request,'base_page/search.html',{'pr':events})







def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password1=request.POST['psw1']
        user=auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request,user)
            print("your login is completed")
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            print("your login is not completed")
            return redirect('login')
    else:
            # User is authenticated
       return render(request,"login.html") 


def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['psw1']
        password2=request.POST['psw2']
        if password1==password2:
            l=n=L=sp=0
            for ch in password1:
                if(len(password1) >=6):
                    if(ch.islower()):
                        l+=1
                    elif(ch.isupper()):
                        L+=1
                    elif(ch.isdigit()):
                        n+=1
                    elif(ch=='#' or ch=='$' or ch=='@'):
                        sp+=1
            if(not(l>= 1 and L>=1 and n>=1 and sp>=1)):
                messages.info(request,"Sorry the password can't meet the constrain!!")
                
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"sorry username already exists!!!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"sorry email taken!!")  
                return redirect('signup')
            else:  
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.info(request,"Your account has been created .You can now login")
                messages.info(request,"Your Username:{},Password{}".format(username,password1))
            return redirect('signup')
        else:
            messages.info(request, "sorry the password did't match!!")
            return redirect('signup')
            
        
    else:
        return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')




def item_detail(request, item_id):
    item = get_object_or_404(Event, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


def delete(request,id):
    obj = Event.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')









