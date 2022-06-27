from django.contrib import admin

from .models import Manga, Images, NewCap, Profile

admin.site.register(Manga)
admin.site.register(Images)
admin.site.register(NewCap)
admin.site.register(Profile)
