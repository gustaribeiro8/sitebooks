from django.shortcuts import render


def book_list(request):
    context = {
        'books': book_data  # Passando os dados dos livros para o template
    }
    return render(request, 'book_list.html', context)

def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)