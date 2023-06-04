from django import forms
from book_app.models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'