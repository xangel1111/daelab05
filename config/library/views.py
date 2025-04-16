from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Book, Author, AuthorProfile, Category, Publisher, Publication
from .forms import BookForm, AuthorForm, AuthorProfileForm, CategoryForm, PublisherForm

# Home View
class HomeView(TemplateView):
    template_name = 'home.html'


# Book Views
class BookListView(ListView):
    model = Book
    paginate_by = 9
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(author__name__icontains=query) |
                Q(isbn__icontains=query)
            )
        return queryset


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    
    def get_success_url(self):
        messages.success(self.request, f'Libro "{self.object.title}" creado con éxito.')
        return reverse_lazy('book_detail', kwargs={'slug': self.object.slug})


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    
    def get_success_url(self):
        messages.success(self.request, f'Libro "{self.object.title}" actualizado con éxito.')
        return reverse_lazy('book_detail', kwargs={'slug': self.object.slug})


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    
    def get_success_url(self):
        messages.success(self.request, f'Libro "{self.object.title}" eliminado con éxito.')
        return super().get_success_url()


# Author Views
class AuthorListView(ListView):
    model = Author
    paginate_by = 9
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class AuthorDetailView(DetailView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['profile_form'] = AuthorProfileForm(self.request.POST, self.request.FILES)
        else:
            context['profile_form'] = AuthorProfileForm()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        
        if profile_form.is_valid():
            self.object = form.save()
            profile = profile_form.save(commit=False)
            profile.author = self.object
            profile.save()
            messages.success(self.request, f'Autor "{self.object.name}" creado con éxito.')
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse_lazy('author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            try:
                profile = self.object.profile
                context['profile_form'] = AuthorProfileForm(
                    self.request.POST, 
                    self.request.FILES, 
                    instance=profile
                )
            except AuthorProfile.DoesNotExist:
                context['profile_form'] = AuthorProfileForm(self.request.POST, self.request.FILES)
        else:
            try:
                profile = self.object.profile
                context['profile_form'] = AuthorProfileForm(instance=profile)
            except AuthorProfile.DoesNotExist:
                context['profile_form'] = AuthorProfileForm()
                
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        
        if profile_form.is_valid():
            self.object = form.save()
            
            try:
                profile = self.object.profile
                profile = profile_form.save()
            except AuthorProfile.DoesNotExist:
                profile = profile_form.save(commit=False)
                profile.author = self.object
                profile.save()
                
            messages.success(self.request, f'Autor "{self.object.name}" actualizado con éxito.')
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse_lazy('author_detail', kwargs={'pk': self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
    
    def get_success_url(self):
        messages.success(self.request, f'Autor "{self.object.name}" eliminado con éxito.')
        return super().get_success_url()


# Category Views
class CategoryListView(ListView):
    model = Category
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    
    def get_success_url(self):
        messages.success(self.request, f'Categoría "{self.object.name}" creada con éxito.')
        return reverse_lazy('category_detail', kwargs={'slug': self.object.slug})


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    
    def get_success_url(self):
        messages.success(self.request, f'Categoría "{self.object.name}" actualizada con éxito.')
        return reverse_lazy('category_detail', kwargs={'slug': self.object.slug})


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    
    def get_success_url(self):
        messages.success(self.request, f'Categoría "{self.object.name}" eliminada con éxito.')
        return super().get_success_url()


# Publisher Views
class PublisherListView(ListView):
    model = Publisher
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class PublisherDetailView(DetailView):
    model = Publisher


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    
    def get_success_url(self):
        messages.success(self.request, f'Editorial "{self.object.name}" creada con éxito.')
        return reverse_lazy('publisher_detail', kwargs={'pk': self.object.pk})


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    
    def get_success_url(self):
        messages.success(self.request, f'Editorial "{self.object.name}" actualizada con éxito.')
        return reverse_lazy('publisher_detail', kwargs={'pk': self.object.pk})


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')
    
    def get_success_url(self):
        messages.success(self.request, f'Editorial "{self.object.name}" eliminada con éxito.')
        return super().get_success_url()