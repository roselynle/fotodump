from django.shortcuts import render
from .models import Category, Photo
# Create your views here.

def gallery(request):
    # get the categories in order to pass them into our template
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photos/gallery.html', context)

def view(request, photo_id):
    return render(request, 'photos/photo.html')

def add(request):
    return render(request, 'photos/addphoto.html')
