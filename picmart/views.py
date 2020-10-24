from django.http import HttpResponse
from django.shortcuts import render, redirect
from picmartapp1.models import *


def show_about_page(request):
    print("about page request")
    name = 'Pankaj'
    link = 'whatever.com'
    data = {
        'name': name,
        'link': link
    }
    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images, 'cats': cats}
    return render(request, "home.html", data)


def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}
    return render(request, "home.html", data)


def home(request):
    return redirect('/home')


def show_search_page(request):
    # return HttpResponse('this is search')
    search = request.GET['search']
    print(search)
    cats = Category.objects.filter(title__icontains=search)
    images = Image.objects.filter(title__icontains=search)
    data = {'images': images, 'cats': cats, 'search': search}
    return render(request, "home.html", data)
