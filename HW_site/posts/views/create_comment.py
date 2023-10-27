# from django.views import View
# from ..models import Posts, Comment
# from django.shortcuts import get_object_or_404, render, redirect
#
#
# class CreateComment(View):
#     def get(self, request):
#         text = Posts.objects.all()
#
#         post = get_object_or_404(Posts)
#
#         comment = Comment(post=post, text=text)
#         comment.save()
#
#         return render(request, 'create_comment.html', {'comment': comment})
# #

#
# class CreateComment(View):
#     def get(self, request):
#         post = Posts.objects.all()
#         return render(request, 'create_comment.html', {'post': post})
#
#     def post(self, request):
#         post = Posts(request.POST)
#         if post.is_valid():
#             post.save()
#             return redirect('all_posts')
#         return render(request, 'create_comment.html', {'post': post})