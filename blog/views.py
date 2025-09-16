from django.shortcuts import render

# Create your views here.

from . import data
from .data import get_post

data.seed()
#domain.com/?q=Football
def post_list(request):
    posts=data.all_posts()
    q=request.GET.get('q')
    if q:
        q_low=q.lower()
        posts=[p for p in posts if q_low in p.title.lower() or q_low in p.content.lower()]

    return render(request,'blog/post_list.html',{"posts":posts})


def post_detail(request,id:int):
    selected_post=get_post(id)

    return render(request,'blog/post_detail.html',{"selected_post":selected_post})


