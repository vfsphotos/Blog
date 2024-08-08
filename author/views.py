from django.shortcuts import redirect, render

from .forms import AuthorForm


def adicionar_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'author/adicionar_author.html', {'form': form})
