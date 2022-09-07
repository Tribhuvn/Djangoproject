from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','Updated','status']
    list_filter=('status','author',)
    search_fields=('title','body',)
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
   

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','Updated','active',)
    list_filter=('active','created','Updated')
    search_fields=('name','email','body')

admin.site.register(Comment,CommentAdmin)