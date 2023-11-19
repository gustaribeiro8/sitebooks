from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label='Título', max_length=100)
    release_year = forms.IntegerField(label='Data de Publicação',
                                      min_value=1888)
    poster_url = forms.URLField(label='URL da Capa', max_length=100)

