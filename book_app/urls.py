from book_app import views
from django.urls import path

app_name = "book_app"
urlpatterns = [
    path('book-list/', views.book_list, name='book_list'),
    path('create/', views.create_book, name='create'),
    path('update/<int:id>', views.update_book, name='update'),
    path('delete/<int:id>', views.delete_book, name='delete')
]
