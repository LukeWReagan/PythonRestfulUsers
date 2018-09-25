
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User

def index(request):
	try:
		users = User.objects.all()
		context = {
			'users' : users
		}
	except NameError:
		context = {}

	return render(request, 'restful/index.html', context)

def show(request, id):
	context = {
		'user' : User.objects.get(id = id)
	}
	return render(request, 'restful/show.html', context)

def new(request):
	return render(request, 'restful/new.html')

def edit(request, id):
	context = {
		'user' : User.objects.get(id = id)
	}
	return render(request, 'restful/edit.html', context)

def create(request):
	new_user = User.objects.create(full_name = request.POST['full_name'], email = request.POST['email'])
	return redirect(reverse('restful:index'))

def update(request, id):
	new_user = User.objects.get(id = id)
	new_user.full_name = request.POST['full_name']
	new_user.email = request.POST['email']
	new_user.save()
	return redirect(reverse('restful:index'))

def destroy(request, id):
	User.objects.filter(id = id).delete()
	return redirect(reverse('restful:index'))