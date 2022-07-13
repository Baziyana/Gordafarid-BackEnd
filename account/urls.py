from django.urls import path, include

app_name = 'account'
urlpatterns = [
    path('auth/', include('djoser.urls')),  # djoser
    path('auth/', include('djoser.urls.jwt')),  # djoser.JWT
]
