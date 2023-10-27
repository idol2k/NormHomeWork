from ..models import Posts
from django.views import View
from django.shortcuts import render


DICT_MAX_CATEGORY = {
    'MY POST': 1,
    'OTHER POST': 3,
    'MORE POSTS': 5
}


class AllPostsView(View):
    def get(self, request):
        posts = Posts.objects.all()
        posts_category = DICT_MAX_CATEGORY
        return render(request, 'all_posts.html', {'posts': posts,
                                                  'posts_category': posts_category})



