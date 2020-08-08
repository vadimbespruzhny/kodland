from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views import View


# Create your views here.


def paginate(request, queryset, num_items):
    paginator = Paginator(queryset, num_items)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {'paginator': paginator, 'items': items}
    return context


class ArticleListView(ListView):
    model = Blog
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Blog.objects.all()
        paginator = paginate(self.request, queryset, 10)
        context['paginator'] = paginator
        for i in queryset:
            context['obj'] = i
        return context


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset


class ArticleCreateView(View):
    form_class = BlogForm
    template_name = 'add_article.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
        return render(request, 'add_article.html', {'form': form})
