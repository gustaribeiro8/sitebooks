from django.forms import ModelForm
from .models import Book, Review, Provider


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Publicação',
            'poster_url': 'URL da Capa',
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
            'service',
            'has_flat_price',
            'price',
        ]
        labels = {
            'service': 'Disponibilidade de compra',
            'has_flat_price': 'FLAT?',
            'price': 'Preço',
        } 
