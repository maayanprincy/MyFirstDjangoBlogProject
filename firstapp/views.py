from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import team,blog
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
	
	
def myblog(request):
	context1={'blog':blog.objects.all()}
	#return render(request,'blog/blog.html',{'title':'Blog'})
	return render(request,'blog/blog.html',context1,{'title':'Blog'})
	

class PostListVw(ListView):
	model=blog
	template_name='blog/blog.html'
	context_object_name='blog'
	ordering=['-date_added']
	paginate_by=5
	
	
class PostDetailVw(DetailView):
	model=blog
	template_name='blog/blog_detail.html'
	context_object_name='blog'
	

class UserPostListVw(ListView):
	model=blog
	template_name='blog/user_posts.html'
	context_object_name='blog'
	paginate_by=5
	 
	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return blog.objects.filter(author=user).order_by('-date_added')
	
	
class PostCreateVw(LoginRequiredMixin, CreateView):
	model=blog
	fields=['title','content']
	template_name='blog/blog_form.html'
	
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
		
		
class PostUpdateVw(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model=blog
	fields=['title','content']
	template_name='blog/blog_form.html'
	
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False
		
		
class PostDeleteVw(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model=blog
	success_url='/blog/'
	template_name='blog/blog_confirm_delete.html'
	context_object_name='blog'
	
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False
