from django.shortcuts import render
from .models import Category, Photo
# Create your views here.

def gallery(request):
    # get the categories in order to pass them into our template
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def view(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    return render(request, 'photos/photo.html', {'photo' : photo})

def add(request):
    return render(request, 'photos/addphoto.html')
