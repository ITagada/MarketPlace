from django.shortcuts import render, redirect
from .models import articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewsDetailView(DetailView):
    model = articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = articles
    template_name = 'news/add_to_cart.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

def news_home(request):
    news = articles.objects.order_by('price')
    return render(request, 'news/news_home.html', {'news': news})



def add_to_cart(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Некорректно заполнена форма'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/add_to_cart.html', data)