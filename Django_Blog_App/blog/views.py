from django.shortcuts import render,get_object_or_404,redirect
from . models import Post
from django.http import HttpResponse
from .forms import BlogPostForm,userRegistationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Post_list(request):
    # return render(request,'blog/index.html')
    responses_data = Post.objects.all()
    return render(request,'blog/index.html',{'posts':responses_data})

def post_detail_page(request,pk):
    post_data = get_object_or_404(Post,pk=pk)
    return render(request,'blog/blog_detail.html',{'data':post_data})
@login_required
def post_new(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post_dataa = form.save()
            return redirect('Post_list')
    else:
        form_dete = BlogPostForm()
    # form_dete = BlogPostForm()
    return render(request,'blog/blog_add_edit.html',{'form_data': form_dete})

def post_edit(request,pk):
    post_data = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,instance=post_data)
        if form.is_valid():
            post_data = form.save()
            return redirect('Post_list')
    else:
        form = BlogPostForm(instance=post_data)
    return render(request,'blog/blog_add_edit.html',{'form_data': form})

def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('Post_list')

def register_user(request):
    if request.method == 'POST':
        form = userRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created Successfully for {username}')
            return redirect('Post_list')
        
    else:
        form = userRegistationForm()
    return render(request,'registration/register.html',{'form':form})