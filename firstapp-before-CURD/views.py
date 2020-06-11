from django.shortcuts import render
from django.http import HttpResponse
from .models import team


# people = [{"firstname":"Corey","lastname": "Schafer" ,"email": "CoreyMSchafer@gmail.com","desc":"CEO & Founder"},
			# {"firstname":"Jane","lastname": "Doe" ,"email": "JaneDoe@gmail.com","desc":"Designer"},
			# {"firstname":"John","lastname": "Doe" ,"email": "JohnDoe@gmail.com","desc":"Architect"}]



def home(request):
	context={'team':team.objects.all()}
	return render(request,'apptemp/home.html',context)

def about(request):
	return render(request,'apptemp/about.html',{'title':'About'})

def login(request):
	return render(request,'apptemp/login.html',{'title':'Login'})