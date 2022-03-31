from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import movie
from.forms import MovieForm


# Create your views here.

def index(request):
    movie_list=movie.objects.all()
    return render(request,'index.html',{'movies':movie_list})

def details(request,movie_id):
    movie_select=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie_select})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        year=request.POST.get('year')
        image=request.FILES['image']
        movies=movie(name=name,description=description,year=year,image=image)
        movies.save()
    return render(request,'add-movies.html')

def update(request,id):
    movies=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':movies})

def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')