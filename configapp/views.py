from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import *
from .forms import *
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

class HomeNews(ListView):
    model=News
    template_name = 'index.html'
    context_object_name = 'news'
    extra_context = {
        'title':'News'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        content=super().get_context_data(**kwargs)
        content['title']='NEWS_LIST'
        content['category']=News.objects.all()
        return content
    def get_queryset(self):
        return News.objects.all()


class HomeCategory(ListView):
    model=News
    template_name = 'category.html'
    context_object_name = 'news'
    extra_context = {
        'title':'News'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        content=super().get_context_data(**kwargs)
        content['title']='CATEGORY_LIST'
        content['categories']=Category.objects.all()
        return content
    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['pk'])

class BlogCreateView(CreateView):
    model = News
    template_name = 'add.html'
    fields = ['title','content','category']

class BlogUpdateView(UpdateView):
    model = News
    template_name = 'update.html'
    fields = ['title','content','category']
class BlogDeleteView(DeleteView):
    model = News
    template_name = 'details.html'
    success_url = reverse_lazy('home')

class SearchResultsView(ListView):
    model = Category
    template_name = 'search.html'
    def get_queryset(self):  # новый
        query = self.request.GET.get('search')
        object_list = Category.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
def moon(request):
    query = Search(request.GET)
    object_list = Category.objects.filter(
        Q(title__icontains=query)
    )
    args = {
        'object_list': object_list
    }
    return render(request, 'search.html',args)

#
# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     content = {
#         'news': news,
#         'categories': categories
#     }
#     return render(request, 'index.html', context=content)
#
#
#
#
# def add_category(request):
#     form = CategoryForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=CategoryForm()
#         return redirect('home')
#     args = {
#         'form': form
#     }
#     return render(request, 'add_category.html',args)

def index(request):
    news=News.objects.all()
    categories=Category.objects.all()
    form1 = SearchForm
    content = {
        'form1':form1,
        'news': news,
        "categories":categories,
    }
    return render(request, 'index.html', context=content)



def categories(request,pk):
    news = News.objects.filter(pk=pk)
    categories = Category.objects.all()

    content = {
        'news': news,
        "categories": categories,
    }
    return render(request, 'home.html', context=content)

def detail(request,pk):
    new=News.objects.get(pk=pk)
    categories=Category.objects.all()
    content={
        "new":new,
        "categories":categories,
    }
    return render(request,'details.html',context=content)


def delete(request,pk):
    new=News.objects.get(pk=pk)
    new.delete()
    return redirect('home')

def boss(request):
    return redirect('add')





def add(request):
         form=NewForm(request.POST or None)
         categories = Category.objects.all()
         new = News.objects.all()
         if form.is_valid():
             form.save()
             return redirect('home')
         content={
            'new':new,
            'form':form,
            'categories':categories
         }
         return render(request,'add.html',context=content)
    #     form = CategoryForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         form=CategoryForm()
    #         return redirect('home')
    #     args = {
    #         'form': form
    #     }
    #     return render(request, 'add_category.html',args)

def edit(request, pk):
    project=News.objects.get(pk=pk)
    # form=NewForm(instance=project)
    if request.method=="POST":
         form=NewForm(request.POST,instance=project)
         if form.is_valid():
             form.save()
             return redirect('home')
    form=NewForm(instance=project)
    content={
        'form':form,
        'project':project,
    }
    return render(request,'update.html',context=content)

def catego(request):
    news = Category.objects.all()
    content = {
        'news': news,

    }
    return render(request, 'category.html', context=content)




def moss(request,pk):
    project=Category.objects.get(pk=pk)
    if request.method=="POST":
         form=Boss(request.POST,instance=project)
         if form.is_valid():
             form.save()
             return redirect('home')
    form = Boss(instance=project)
    form1 = SearchForm
    content={
        'form1':form1,
        'form':form,
        'project':project
    }
    return render(request,'mossa.html',context=content)



def add_category(request):
    form = Boss(request.POST or None)
    if form.is_valid():
        form.save()
        form=Boss()
        return redirect('home')
    args = {
        'form': form
    }
    return render(request, 'add_category.html',args)

# def add_category(request):
#     form = CategoryForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=CategoryForm()
#         return redirect('home')
#     args = {
#         'form': form
#     }
#     return render(request, 'add_category.html',args)

