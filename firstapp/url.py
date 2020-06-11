from django.urls import path
from . import views
from .views import PostListVw,PostDetailVw,PostCreateVw,PostUpdateVw,PostDeleteVw,UserPostListVw


urlpatterns = [
    path('', views.home,name="Home-Page"),
	path('about/', views.about,name="About-Page"),
	path('login/', views.login,name="login-Page"),
	path('blog/', PostListVw.as_view(),name="blog"),
	path('blog/user/<str:username>/', UserPostListVw.as_view(),name="user-posts"),
	path('blog/<int:pk>/', PostDetailVw.as_view(),name="post-detail"),
	path('blog/new/', PostCreateVw.as_view(),name="post-create"),
	path('blog/<int:pk>/update/', PostUpdateVw.as_view(),name="post-update"),
	path('blog/<int:pk>/delete/', PostDeleteVw.as_view(),name="post-delete"),
]