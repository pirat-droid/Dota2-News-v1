from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopnewsView.as_view(), name='home'),
    path('news/<int:pk>/', views.NewsDetail.as_view(), name='post_detail'),
    path('news/', views.AllNews.as_view(), name='all_news'),
    path('archiv-stream/', views.ArchivStream.as_view(), name='all_stream'),
    path('tournament/', views.Tournament.as_view(), name='all_tournament'),
    path('tournament/<int:pk>/', views.TournamentDetail.as_view(), name='tournament_detail'),
    path('comand/<int:pk>/', views.ComandDetail.as_view(), name='comand_detail')
]