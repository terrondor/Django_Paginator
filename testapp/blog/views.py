from django.shortcuts import render

from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})
