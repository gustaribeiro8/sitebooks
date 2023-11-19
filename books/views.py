from django.http import HttpResponseRedirect
from .temp_data import book_data
from .models import Book
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'books/detail.html', context)

def list_books(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'books/index.html', context)

def search_books(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        book_list = Book.objects.filter(name__icontains=search_term)
        context = {"book_list": book_list}
    return render(request, 'books/search.html', context)

def create_book(request):
    if request.method == 'POST':
        book_name = request.POST['name']
        book_release_year = request.POST['release_year']
        book_poster_url = request.POST['poster_url']
        book = Book(name=book_name,
                      release_year=book_release_year,
                      poster_url=book_poster_url)
        book.save()
        return HttpResponseRedirect(
            reverse('books:detail', args=(book.id, )))
    else:
        return render(request, 'books/create.html', {})


def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.name = request.POST['name']
        book.release_year = request.POST['release_year']
        book_poster_url = request.POST['poster_url']
        book.save()
        return HttpResponseRedirect(
            reverse('books:detail', args=(book.id, )))

    context = {'book': book}
    return render(request, 'books/update.html', context)


def delete_books(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect(reverse('books:index'))

    context = {'book': book}
    return render(request, 'books/delete.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/index.html'
