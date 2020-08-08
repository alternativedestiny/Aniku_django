from django.db import models
from django.contrib.auth.models import User

img = 'D://PersonalProject//Aniku_django//templates//img'


# 电影
class Movie(models.Model):
    name_cn = models.CharField(max_length=100, default='')  # 中文名
    name_en = models.CharField(max_length=100, default='', blank=True)  # 英文名
    publish_y = models.IntegerField(default=1900, blank=True)  # 年份
    poster = models.CharField(max_length=50, default='', blank=True)  # 封面
    director = models.CharField(max_length=50, default='', blank=True)  # 导演
    starring = models.CharField(max_length=100, default='', blank=True)  # 主演
    tags = models.CharField(max_length=100, default='', blank=True)  # 标签
    path = models.CharField(max_length=100, default='', blank=True)  # 路径
    size = models.FloatField(default=0)  # 大小
    db_id = models.CharField(max_length=20, default='', blank=True)  # 豆瓣电影id

    def __str__(self):
        return self.name_cn


class Tv(Movie):
    seasons = models.IntegerField(default=1, null=True)  # 共几季
    season = models.IntegerField(default=1, null=True)  # 当前季
    parts = models.IntegerField(default=1)  # 总集数
    part = models.IntegerField(default=1)  # 集


# 动漫、剧
class Animation(models.Model):
    name_cn = models.CharField(max_length=100, default='')  # 中文名
    name_en = models.CharField(max_length=100, default='')  # 英文名
    publish_y = models.IntegerField(default=1900, null=True)  # 年份
    seasons = models.IntegerField(default=1, null=True)  # 共几季
    season = models.IntegerField(default=1, null=True)  # 当前季
    part = models.IntegerField(default=1)  # 集
    poster = models.FileField(null=True)  # 封面
    director = models.CharField(max_length=50, default='', blank=True)  # 监督
    staff = models.CharField(max_length=100, default='', blank=True)  # 声优/演员
    tags = models.CharField(max_length=100, default='', blank=True)  # 标签
    path = models.FilePathField(path=img, allow_folders=True, default='')  # 路径
    size = models.FloatField(default=0)  # 大小
    douban_id = models.CharField(max_length=20, default='')  # 豆瓣电影id

    def __str__(self):
        return self.name_cn
