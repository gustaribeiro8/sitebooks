from django.contrib import admin

from .models import Book, Review, List, Provider

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(List)
admin.site.register(Provider)
