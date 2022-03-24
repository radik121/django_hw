from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    catalog = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': [c for c in catalog]
    }
    return render(request, template, context)


def one_book_view(request, pub_date):
    book = Book.objects.get(pub_date=pub_date)
    try:
        prev_date = Book.objects.order_by('-pub_date').filter(pub_date__lt=pub_date)[0:1].get()
    except Book.DoesNotExist:
        prev_date = Book.objects.order_by('-pub_date')[0:1].get()
    try:
        next_date = Book.objects.order_by('pub_date').filter(pub_date__gt=pub_date)[0:1].get()
    except Book.DoesNotExist:
        next_date = Book.objects.order_by('pub_date')[0:1].get()
    template = 'books/one_book.html'
    context = {
        'book': book,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    # print(prev_date)
    return render(request, template, context)
