import datetime
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.shortcuts import render,redirect
from django.contrib import auth,messages
from .forms import UserRegistrationForm,UserUpdateForm,UserUpdateForm2
from django.contrib.auth.decorators import login_required
from .models import User
from Posts.models import Post

def signup(request):
    if request.method == "POST":
      form=UserRegistrationForm(request.POST)
      if form.is_valid():
          form.save()
          username=form.cleaned_data.get('username')
          first_name = form.cleaned_data.get('first_name')
          last_name = form.cleaned_data.get('last_name')
          messages.success(request,f'Account created for {username}')
          return redirect('Home')
    else:
        form = UserRegistrationForm()
    return render(request, "Users/signup.html", {'title': "Signup",'form':form})

@login_required
def profile(request):
    post = Post.objects.all()
    if request.method == "POST":
     u_form=UserUpdateForm(request.POST,instance=request.user)
     i_form = UserUpdateForm2(request.POST,request.FILES,instance=request.user.profile)
     if u_form.is_valid() and i_form.is_valid():
         u_form.save()
         i_form.save()
         messages.success(request, f'Data updated successfully')
    else:
        u_form = UserUpdateForm(instance=request.user)
        i_form = UserUpdateForm2(instance=request.user.profile)
    context={
        'title': "Profile",
        'posts':post,
        'u_form':u_form,
        'i_form':i_form,

    }
    return render(request, "Users/profile.html", context)

class profile_view(DetailView):
    model=User

