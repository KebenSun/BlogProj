from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
import json

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    """提交评论"""
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            comtext = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', comtext=comtext)
    return redirect(post)

def comment_likes(request):
    """json测试"""
    #comment = get_object_or_404(Comment, pk=comment_pk)

    resp = {'code': 0, 'msg': '点赞成功'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
