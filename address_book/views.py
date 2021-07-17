from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import AddressBook


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def add_address(request):
    return render(request, 'add_address.html', {})


# Here I'm going to create a list view for all
class AddressList(ListView):
    template_name = 'address_list.html'
    model = AddressBook

    def get_context_data(self, **kwargs):
        context = super(AddressList, self).get_context_data(**kwargs)
        addresses = AddressBook.objects.all()
        context['addresses'] = addresses
        return context
