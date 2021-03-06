from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','score')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','full_name','addr','qq','email')
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)