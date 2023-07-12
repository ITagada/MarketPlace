from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]