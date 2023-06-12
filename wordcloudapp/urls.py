from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_wordcloud/', views.generate_wordcloud, name='generate_wordcloud'),
    path('download_wordcloud/', views.download_wordcloud, name='download_wordcloud'),
]
