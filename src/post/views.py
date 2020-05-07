from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from .models import Post
# Create your views here.

#def home(*args,**kwargs) :
#	return HttpResponse("<h1>Hi Everyone</h1>")

def postview(request):
	form =PostForm(request.POST or None)
	if form.is_valid():
		form.save()

	context={
	    'form' : form
	}
	return render(request,"post/post_create.html",context)

'''def postview(request) :
	form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= PostForm()

    context = {
        'form': form
    }        	
    return render(request,"post/post_create.html",context)'''

