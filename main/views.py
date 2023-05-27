from django.shortcuts import render, redirect

from .models import *   # main/models.py-დან ყველა მოდელის იმპორტი

menu = SiteMenu.objects.all()


def index(request):
    context = {
        'menu': menu,   
        'title': menu[0].title,
        'is_visible': menu[0].is_visible,
        'is_active': True,
        # 'children': menu[0].children.all(),
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'menu': menu,
        'title': menu[2].title,
        'is_visible': menu[2].is_visible,
        'is_active': True,
        # 'children': menu[2].children.all(),
    }
    return render(request, 'main/about.html', context=context)

def contact(request):
    context = {
        'menu': menu,
        'title': menu[3].title,
        'is_visible': menu[3].is_visible,
        'is_active': True,
        # 'children': menu[2].children.all(),
    }
    return render(request, 'main/contact.html',context=context)

def reg(request):
    context = {
        'menu': menu,
        'title': menu[1].title,
        'is_visible': menu[1].is_visible,
        'is_active': True,
        # 'children': menu[1].children.all(),
    }
    return render(request, 'main/reg.html',context=context)
