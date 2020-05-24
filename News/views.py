from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import PostModel, ComandModel, GameArchivModel, ReitingModel, LiveStreamModule, ArchivStreamModule, TournamentModule

# Create your views here.

class Stream:
    """Enter strim page home"""
    def get_stream(self):
        return LiveStreamModule.objects.all()[:3]

class Post:
    """Вывод не топовых новостей"""
    def get_post(self):
        return PostModel.objects.filter(top=False, pub=True)[:4]

class Game:
    """Вывод предстоящих игр"""
    def get_game(self):
        return GameArchivModel.objects.filter(closed=False)[:8]

class Reiting:
    """Рейтинг команд"""
    def get_reiting(self):
        return ReitingModel.objects.all()


class TopnewsView(ListView, Post, Game, Reiting, Stream):
    model = PostModel
    queryset = PostModel.objects.filter(top=True, pub=True)[:2]


class NewsDetail(DetailView, Game, Reiting):
    """Подробней о новности"""
    model = PostModel

class AllNews(ListView, Game, Reiting):
    model = PostModel
    template_name = 'News/all_news.html'
    paginate_by = 6
    queryset = PostModel.objects.filter(pub=True)

class ArchivStream(ListView, Game, Reiting):
    """Archiv twitch stream"""
    model = ArchivStreamModule
    template_name = 'News/all_stream.html'
    paginate_by = 6
    queryset = ArchivStreamModule.objects.all()

class Tournament(ListView, Game, Reiting):
    """ARchiv  tournament"""
    model = TournamentModule
    template_name = 'News/all_tournament.html'
    paginate_by = 6
    queryset = TournamentModule.objects.all()

class TournamentDetail(DetailView, Game, Reiting):
    """Подробнее о турнире"""
    model = TournamentModule
    template_name = 'News/tournament_detail.html'

class ComandDetail(DetailView, Game, Reiting):
    """Подробнее о турнире"""
    model = ComandModel
    template_name = 'News/comand_detail.html'