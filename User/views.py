from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm
from Movie.views import movie_list
def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return movie_list(request)
                else:
                    return HttpResponse('your account is disabled')
            else:
                context={'form':form,'user':user}
                return render(request,'User/login.html',context)
    else:
        form=LoginForm()
    context={'form':form}
    return render(request,'User/login.html',context)
def sign_up(request):
    if request.method=='POST':
        u_form=SignUpForm(request.POST)
        if u_form.is_valid():
            new_user=u_form.save(commit=False)
            new_user.set_password(u_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse('User Registration Done')
    else:
        u_form=SignUpForm()
    context={'form':u_form}
    return render(request,'User/signup.html',context)
def log_out(request):
    logout(request)
    return movie_list(request)