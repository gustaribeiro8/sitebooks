from django.http import HttpResponseRedirect
from .temp_data import book_data
from .models import Book, Review, List, Provider
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import BookForm, ReviewForm, ProviderForm

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
        book_form = BookForm(request.POST)
        provider_form = ProviderForm(request.POST)
        if book_form.is_valid():
            book = Book(**book_form.cleaned_data)
            book.save()
            if provider_form.is_valid(
            ) and provider_form.cleaned_data['service']:
                provider = Provider(book=book, **provider_form.cleaned_data)
                provider.save()
            return HttpResponseRedirect(
                reverse('books:detail', args=(book.pk, )))
    else:
        book_form = BookForm()
        provider_form = ProviderForm()
    context = {'book_form': book_form, 'provider_form': provider_form}
    return render(request, 'books/create.html', context)

def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book.name = form.cleaned_data['name']
            book.release_year = form.cleaned_data['release_year']
            book.poster_url = form.cleaned_data['poster_url']
            book.save()
            return HttpResponseRedirect(
                reverse('books:detail', args=(book.id, )))
    else:
        form = BookForm(
            initial={
                'name': book.name,
                'release_year': book.release_year,
                'poster_url': book.poster_url
            })

    context = {'book': book, 'form': form}
    return render(request, 'books/update.html', context)

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect(reverse('books:index'))

    context = {'book': book}
    return render(request, 'books/delete.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/index.html'


def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            movie=book)
            review.save()
            return HttpResponseRedirect(
                reverse('books:detail', args=(book_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'book': book}
    return render(request, 'books/review.html', context)

class ListListView(generic.ListView):
    model = List
    template_name = 'books/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'books/create_list.html'
    fields = ['name', 'author', 'books']
    success_url = reverse_lazy('books:lists')

