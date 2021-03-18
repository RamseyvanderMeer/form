from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact(request):

    
    form = ContactForm()
    return render(request, 'form.html', {'form' : form})