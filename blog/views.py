from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect


def homeblog(request):
#   return redirect('article-detail',{'pk':1})
    return redirect(reverse('article-detail', kwargs={'pk':1}))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
#   ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts =  Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-',' ').lower(),'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
#   fields = ('title','body')
#   fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
#   fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    fields = '__all__'


class CategoryHomeView(ListView):
    model = Category
    template_name = 'category_list.html'
    ordering = ['-id']

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')
