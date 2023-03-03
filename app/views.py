from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    return render(request,'app/index.html')

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

class AllPostsView(ListView):
    model = Post
    template_name = 'app/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.order_by('-created_on')



class PostDetailView(DetailView):
    model = Post
    template_name = "app/post_detail.html"        
