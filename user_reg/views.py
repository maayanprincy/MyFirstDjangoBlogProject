from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegFrm,UserUpdateFrm,UserProfileFrm
# Create your views here.

def register(request):
	if request.method=="POST":
		form=UserRegFrm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get("username")
			messages.success(request,f'Account Created for Successfully!, u are now able to log in')
			return redirect('login') 
	else:
		form=UserRegFrm()
	return render(request,'user_reg/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=="POST":
		u_form=UserUpdateFrm(request.POST,instance=request.user)
		p_form=UserProfileFrm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your Account has been updated Sucessfully!')
			return redirect('profile') 
	else:
		u_form=UserUpdateFrm(instance=request.user)
		p_form=UserProfileFrm(instance=request.user.profile)
	context={'u_form':u_form,'p_form':p_form}
	return render(request,'user_reg/profile.html',context)