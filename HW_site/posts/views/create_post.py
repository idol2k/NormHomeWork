from django.shortcuts import render, redirect
from django.views import View
from ..forms import PostsForm

class CreatePostView(View):
    def get(self, request):
        form = PostsForm()
        return render(request, 'create_post.html', {'form': form})

    def post(self, request):
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
        return render(request, 'create_post.html', {'form': form})