from django.shortcuts import render,get_object_or_404
from blog.models import post

# Create your views here.
def post_list_view(request):
    post_list=post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,Post):
    post=get_object_or_404(post,slug=Post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post_detail.html',{'post':post})
