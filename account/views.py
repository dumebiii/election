from django.db.models.fields import CharField
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages

from django.http import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import auth







def register(request):
    
    
        if request.method == "POST":
            name = request.POST['name']
            name2 = request.POST['name2']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
                return render(request, "register.html")

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=name , last_name=name2)
                user.save()
                userp = User.objects.get(email=email)
                userp.save()
                r_user = request.user
            if r_user.is_authenticated:
                 return redirect("thanks")
            else:
                 messages.success(request, 'Regsistered succesfully')

              
        return render(request, "register.html")
    

def thanks(request):
    return render(request, 'thanks.html' )

def loginn(request):
    
        if request.method == "POST":
            password = request.POST['password']
            email = request.POST['email']

            if User.objects.filter(email=email).exists():
                c_user = User.objects.get(email=email)
                username = c_user.username
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect("profile")
                else:
                  messages.error(request, 'Wrong email or password, abeg recheck am ')
                  return render(request, "index.html")
            else:
                 messages.error(request, 'Email not found')
                 return render(request, "index.html")
        else:   
             return render(request, 'index.html')

def profile(request):
   
    return render(request, 'main.html', )






    #  if request.method =='POST':
    #  form = Register(request.POST)
    #  if form.is_valid():
    #      form.save()
    #      username = form.cleaned_data.get('username')
    #      messages.success(request, f'Hi,{username}, your account has been created succesfully')
    #      return redirect ('thanks')
    # else:
    #     form = Register()


   
    # context = {'form':form}
