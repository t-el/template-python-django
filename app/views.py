from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def mit(request):
    return render(request,'app/license.html')    

def creat_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request,'app/create_post.html',{'form':form}) 
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid():
            form.save()
            return  redirect('app/posts')

def about_site(request):
    return render(request,'app/about_site.html')


from django.db.models import Q
class AllPostsView(ListView):
    model = Post
    template_name = 'app/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')

        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | Q(content__icontains=search_term)
            )

        if category:
            queryset = queryset = queryset.filter(categories__pk=category)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('search')
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = "app/post_detail.html"        
