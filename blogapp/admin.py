from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    list_display = ('author','title','publish','status')
    list_filter = ('author','status','publish','created')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')