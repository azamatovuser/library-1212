from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book
from book.forms import BookForm


def index(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "index.html", context)


def detail(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    context = {
        "book": book
    }
    return render(request, 'detail.html', context)


def update(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("detail", pk)
    context = {
        "form": form,
    }
    return render(request, "update.html", context)


def create(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request, "create.html", context)


def delete(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    if request.method == "POST":
        book.delete()
        return redirect("index")
    return render(request, "delete.html")