from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('', views.login_view, name='root_login'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # keep your book views too
    path('books/', views.all_books, name='all_books'),
    path('books/expensive/', views.expensive_books, name='expensive_books'),
    path('books/count/', views.book_count, name='book_count'),
]
