from django.shortcuts import redirect, render
from .models import Publication

from .forms import PublicationForm


def index(request):
    publications = Publication.objects.all()

    return render(request, 'index.html', {'publications': publications})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')


def adicionar_publication(request):
    if request.method == 'POST':
        forms = PublicationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = PublicationForm()
    return render(request, 'publication/adicionar_publication.html', {'forms': forms})
