from django.shortcuts import render

from .models import Author
from library.models import Book
from datetime import datetime

def all_authors(request):
    return render(request, 'authors/all_authors.html')

def book_signings(request):
    return render(request, 'authors/book_signings.html')

def authors_books(request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    sorted_authors = Author.objects.order_by('first_name')
    balogun = Author.objects.get(first_name="Balogun", last_name="Damilola")
    sugar_girls_book= Book.objects.get(title="Sugar girls", author=balogun)
    recently_published = Book.objects.order_by("-published_on")
    year_2023 = datetime(2023, 1, 1)
    new_published = all_books.filter(published_on__gt=year_2023)
    context = {
        'all_the_authors': all_authors,
        'all_the_books': all_books,
        'sorted_the_authors': sorted_authors,
        'sugar_girls': sugar_girls_book,
        'recently_published': recently_published,
        'new_published': new_published,
    }
    return render(request, 'authors/authors-books.html', context)
    