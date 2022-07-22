from blog import views
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('list/', views.PostList.as_view(), name='list'),
    path('detail/<slug>', views.PostDetail.as_view(), name='detail'),
]
