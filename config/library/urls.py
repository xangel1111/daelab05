from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.HomeView.as_view(), name='home'),
    
    # Book URLs
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/add/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<slug:slug>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<slug:slug>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    
    # Author URLs
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    
    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<slug:slug>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<slug:slug>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Publisher URLs
    path('publishers/', views.PublisherListView.as_view(), name='publisher_list'),
    path('publishers/add/', views.PublisherCreateView.as_view(), name='publisher_create'),
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers/<int:pk>/edit/', views.PublisherUpdateView.as_view(), name='publisher_update'),
    path('publishers/<int:pk>/delete/', views.PublisherDeleteView.as_view(), name='publisher_delete'),
]