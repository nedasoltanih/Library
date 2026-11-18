from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context["readers"] = context["book"].reader_set.all()
        return context