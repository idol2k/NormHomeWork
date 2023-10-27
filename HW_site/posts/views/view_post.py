from django.views import View
from django.shortcuts import get_object_or_404, render
from ..models import Posts

class VIewPost(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, pk=post_id)
        return render(request, 'view_post.html', {'post': post})