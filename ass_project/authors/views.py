from django.shortcuts import render

def all_authors(request):
    return render(request, 'authors/all_authors.html')

def book_signings(request):
    return render(request, 'authors/book_signings.html')