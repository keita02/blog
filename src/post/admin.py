from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Author, Banner, Comment, PostView
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = [ 'id' ,'title', 'author']
	list_filter = ('author', )
	list_display_links = [ 'id' ,'title']
	ordering = ('-timestamp', )

class BannerAdmin(admin.ModelAdmin):
	list_display = ('banner_text', )

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'timestamp']

	
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostView)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.unregister(Group)
admin.site.site_header = 'Blog'
admin.site.site_title = 'Blog'
