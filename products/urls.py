from django.urls import path
from . import views


urlpatterns = [
	# name parameter is useful when refering view in tamplate
	path('signup', views.signup, name='signup'),
	path('signin', views.signin, name='signin'),
	path('hello/', views.hello, name='hello'),
	path('logout', views.logout, name='logout'),
	path('create_post', views.post_blog, name='create_post'),
	path('feed/', views.feed),
	path('', views.mainpage),
]
