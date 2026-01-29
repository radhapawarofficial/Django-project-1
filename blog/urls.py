from django.urls import path
from .views import PostListView, django-faq_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('django-faq/', django-faq_view, name='django-faq'),
]