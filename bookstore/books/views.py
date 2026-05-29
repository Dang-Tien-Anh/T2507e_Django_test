from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book

# --- Exercise 1: Book views ---
def all_books(request):
    books = Book.objects.all()
    return render(request, 'books/all_books.html', {'books': books})

def expensive_books(request):
    books = Book.objects.filter(price__gt=100)
    return render(request, 'books/expensive_books.html', {'books': books})

def book_count(request):
    count = Book.objects.count()
    return render(request, 'books/book_count.html', {'count': count})


# --- Exercise 2: Authentication views ---
def login_view(request):
    # If already logged in, redirect root "/" to dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "books/login.html", {"error": "Invalid credentials"})
    return render(request, "books/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "books/dashboard.html", {"username": request.user.username})
