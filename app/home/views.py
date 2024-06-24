from django.core.paginator import Paginator
from django.shortcuts import render

posts = list(range(1000))

def home(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'home/pages/index.html',
        {
            'page_obj': page_obj
        }
    )


def page(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'home/pages/page.html',
        {
            'page_obj': page_obj
        }
    )


def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'home/pages/post.html',
        {
            'page_obj': page_obj
        }
    )
