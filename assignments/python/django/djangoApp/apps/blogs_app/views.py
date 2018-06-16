from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	print ('in index function')
	return HttpResponse('INDEX this is a httpResponse')
	#return render(request,'blogs_app/index.html') #supposed to be via httpResponse


def new(request):
	return HttpResponse('NEW placeholder to display a new form to create a new blog')

def create(request):
	return redirect('/')

def show(request, number):
	return HttpResponse('placeholder to display blog {{number}}')

