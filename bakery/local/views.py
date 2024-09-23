from django.shortcuts import render


def home(request):
    return render(request, 'local/home.html')

def about(request):
    return render(request, 'local/about.html')

def menu(request):
    return render(request, 'local/menu.html')

def contact(request):
    return render(request, 'local/contact.html')
