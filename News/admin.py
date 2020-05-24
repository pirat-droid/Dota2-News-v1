from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import PostModel, PlayerModel, ComandModel, CountryModel, ReitingModel, TournamentModule, LiveStreamModule, GameArchivModel, ArchivStreamModule

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'get_image', 'top', 'pub')
    list_filter = ('date', 'top', 'pub')
    search_fields = ('title', 'date')
    list_editable = ('top', 'pub')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="82" height="50">')

    get_image.short_description = "Постер"

@admin.register(PlayerModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nikname', 'get_photo', 'comand')
    search_fields = ('name', 'nikname', 'comand')
    list_filter = ('comand',)

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')

    get_photo.short_description = "Изображение"

@admin.register(ComandModel)
class ComandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'get_logo')
    list_filter = ('country',)
    search_fields = ('name', 'country')

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="50" height="60">')

    get_logo.short_description = "Логотип"

@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_flag')

    def get_flag(self, obj):
        return mark_safe(f'<img src={obj.flag.url} width="50" height="60">')

    get_flag.short_description = "Флаг"

@admin.register(ReitingModel)
class ReitingAdmin(admin.ModelAdmin):
    list_display = ('place','comand', 'reiting')
    list_filter = ('date',)
    search_fields = ('comand',)

@admin.register(TournamentModule)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_logo', 'prize_pool', 'closed')
    search_fields = ('name',)
    list_editable = ('closed',)

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="110" height="50">')

    get_logo.short_description = "Логотип"

@admin.register(GameArchivModel)
class GameArchivAdmin(admin.ModelAdmin):
    list_display = ('name_match', 'comand1', 'comand1_map', 'comand2_map', 'comand2', 'date', 'closed')
    list_filter = ('date', 'name_match', 'closed')
    search_fields = ('name_match',)
    list_editable = ('closed',)

@admin.register(LiveStreamModule)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ("title",)

@admin.register(ArchivStreamModule)
class ArchivStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'name_chanel', 'name_matches', 'comand_name1', 'comand_name2')
    search_fields = ('title', 'name_chanel', 'name_matches', 'comand_name1', 'comand_name2')
    list_filter = ('name_chanel', 'name_matches', 'date')