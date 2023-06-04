from django.shortcuts import render, redirect
from book_app.models import Book
from .forms import Bookform
# Create your views here.
def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'book_list.html', context={'all_book':book_list})

def create_book(request):
    if request.method == "POST":
        form = Bookform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_app:book_list')
            except:
                pass
    else:
        form = Bookform()   
        
    return render(request, 'create.html', context={'form':form})

def update_book(request, id):
    book = Book.objects.get(id=id)
    form = Bookform(initial={'book_name': book.book_name, 'author':book.author, 'description':book.description})
    
    if request.method == "POST":
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_app:book_list')
            except Exception as e:
                pass    
        
    return render(request, 'update.html', {'form':form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book_app:book_list')