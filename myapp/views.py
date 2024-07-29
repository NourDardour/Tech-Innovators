from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Company

def home(request):
    companies = Company.objects.all()
    form = ContactForm()
    return render(request, 'home.html', {'companies': companies, 'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')
