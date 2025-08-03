from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testApp.models import BookModel

# Create your views here.

class BookList(ListView):
    model= BookModel
    template_name= 'testApp/books.html'
    context_object_name= 'books'

class BookDetails(DetailView):
    model= BookModel
    template_name= 'testApp/bookdetails.html'
    context_object_name= 'books'

class BookCreate(CreateView):
    model= BookModel
    fields= '__all__'

class BookUpdate(UpdateView):
    model= BookModel
    template_name= "testApp/bookupdate.html"
    fields= '__all__'
    # fields= ('pages', 'price')

from django.urls import reverse_lazy
class BookDelete(DeleteView):
    model= BookModel
    success_url= reverse_lazy('booklist')