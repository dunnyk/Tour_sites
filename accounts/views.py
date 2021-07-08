from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth #auth is used for log-in, user help to hold data like username like here below



def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created') #show this to show change on the page
                return redirect('login')
        else:
            messages.info(request, 'password not matching.....')
            return redirect('register')

        return redirect('/travello') #want to call the home  page again, use redirect('/') import it from django like above.

    else:
        return render(request,'register.html')


def login(request):
    if request.method == "POST":
        # return render(request,'login.html')
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            print("logged in succefully")
            return redirect("/travello")
        else:
            print("invalid credentials")
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/travello")