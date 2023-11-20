from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('search/', views.search_books, name='search'),
    path('<int:book_id>/', views.detail_book, name='detail'),
    path('create/', views.create_book, name='create'),
    path('update/<int:book_id>/', views.update_book, name='update'),
    path('delete/<int:book_id>/', views.delete_book, name='delete'),
    path('<int:book_id>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),

]