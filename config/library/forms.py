from django import forms
from .models import Book, Author, AuthorProfile, Category, Publisher, Publication


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
        help_texts = {
            'slug': 'Identificador único para URL. Dejar en blanco para generarlo automáticamente.',
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'death_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'death_date': forms.DateInput(attrs={'type': 'date'}),
        }


class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ['biography', 'website', 'photo']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 6}),
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'website']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['book', 'publisher', 'publication_date', 'edition']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'subtitle', 'slug', 'author', 
            'isbn', 'publication_date', 'page_count',
            'cover', 'summary', 'categories'
        ]
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'summary': forms.Textarea(attrs={'rows': 5}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'slug': 'Identificador único para URL. Dejar en blanco para generarlo automáticamente.',
        }