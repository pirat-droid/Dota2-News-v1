import datetime

from django.db import models

class CountryModel(models.Model):
    name = models.CharField("Название страны", max_length=50)
    flag = models.ImageField("Флаг", upload_to='flags/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Старан"
        verbose_name_plural = "Страны"

class ComandModel(models.Model):
    name = models.CharField("Имя команды", max_length=50)
    logo = models.ImageField("Логотип команды", upload_to='logo/')
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class PlayerModel(models.Model):
    name = models.CharField("Имя игрока", max_length=100)
    nikname = models.CharField("Ник игрока", max_length=100, default='')
    photo = models.ImageField("Фото игрока", upload_to='players/')
    comand = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

class ReitingModel(models.Model):
    place = models.SmallIntegerField("Место команды", default=0)
    reiting = models.SmallIntegerField("Рейтинг команды", default=0)
    comand = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.place} - {self.comand}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class TournamentModule(models.Model):
    name = models.CharField("Название матча", max_length=100)
    logo = models.ImageField("Логотип матча", upload_to='logo/')
    prize_pool = models.SmallIntegerField("Призовой фонд", null=False, default=0)
    description = models.TextField("Описание турнира", max_length=500, null=False)
    comand = models.ManyToManyField(ComandModel, verbose_name="Команды", related_name="comand_tournament")
    closed = models.BooleanField("Закончился", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"

class GameArchivModel(models.Model):
    name_match = models.ForeignKey(TournamentModule, on_delete=models.SET_NULL, null=True)
    comand1 = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True, related_name="comand_one")
    comand2 = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True, related_name="comand_two")
    comand1_map = models.CharField("Выигранных карт 1 командой", max_length=1, default='0')
    comand2_map = models.CharField("Выигранных карт 2 командой", max_length=1, default='0')
    date = models.DateField("Дата проведения игры", null=False)
    closed = models.BooleanField("Закончился", default=False)

    def __str__(self):
        return f"{self.name_match}"

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class PostModel(models.Model):
    title = models.CharField("Название поста", max_length=100)
    image = models.ImageField("Постер", upload_to='post/', default='')
    text = models.TextField("Текст поста")
    date = models.DateField("Дата")
    top = models.BooleanField("Главнй пост", default=False)
    pub = models.BooleanField("Опубликован", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class LiveStreamModule(models.Model):
    title = models.CharField("Название стрима", max_length=150)
    link = models.CharField("Ссылка на стрим", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ":Живой стрим"
        verbose_name_plural = "Живые стримы"

class ArchivStreamModule(models.Model):
    title = models.CharField("Название стрима", max_length=150)
    name_chanel = models.CharField("Название канала", max_length=150)
    date = models.DateField("Дата стрима", null=False)
    name_matches = models.ForeignKey(TournamentModule,  on_delete=models.SET_NULL, null=True, related_name="match_name")
    link = models.CharField("Ссылка на стрим", max_length=500)
    comand_name1 = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True, related_name="comand_1")
    comand_name2 = models.ForeignKey(ComandModel, on_delete=models.SET_NULL, null=True, related_name="comand_2")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Архивный стрим"
        verbose_name_plural = "Архив стримов"