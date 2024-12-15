from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Postlarni ro'yxatini ko'rsatish
    path('', views.PostListView.as_view(), name='post_list'),

    # Postning batafsil ko'rinishini ko'rsatish
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),

    # Postni baham ko'rish uchun yo'nalish
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
