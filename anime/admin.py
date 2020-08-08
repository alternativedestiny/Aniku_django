from django.contrib import admin
from .models import *  # 从models.py引入所有模型


# Register your models here.
class AnimationAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_en', 'director')


class TvAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_en', 'director')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_en', 'director')


admin.site.register(Animation, AnimationAdmin)
admin.site.register(Tv, TvAdmin)
admin.site.register(Movie, MovieAdmin)
