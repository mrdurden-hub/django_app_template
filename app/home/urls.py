
from django.urls import path
from home.views import home, post, page

urlpatterns = [
    path('', home, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),

]
