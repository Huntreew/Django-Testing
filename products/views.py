from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


from django.http import HttpResponse
from .models import Post


@login_required(login_url="signin")
def mainpage(request):
	return render(request, "mymainpage.html")


@login_required(login_url="signin")
def hello(request):
	return HttpResponse("<html><body>Dobry den</body></html>")


@login_required(login_url="signin")
def feed(request):
	return HttpResponse("<html><body>Tohle je feed</body></html>")


@login_required(login_url="signin")
def post_blog(request):

	if request.method == "POST":
		title = request.POST.get("title", None)
		text = request.POST.get("text", None)

		post = Post.objects.create(title=title, text=text)
		post.save()

		return redirect("create_post")

	else:
		return render(request, "mycreate_post.html")


def signin(request):

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Credentials Invalid")
			return redirect("signin")

	else:
		return render(request, "mysignin.html")


def signup(request):

	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST.get("password", None)
		password2 = request.POST[ "password2"]

		if password == password2:

			if User.objects.filter(email=email).exists():
				messages.info(request, "email taken")
				return redirect("signup")

			elif User.objects.filter(username=username).exists():
				messages.info(request, "username taken")
				return redirect("signup")

			else:
				user = User.objects.create_user(username=username, password=password, email=email)
				user.save()
				return redirect("hello")

		else:
			messages.info(request, "password not match")
			return redirect("signup")

	else:
		return render(request, "mysignup.html")

@login_required(login_url="signup")
def logout(request):
	auth.logout(request)
	return redirect("signin")