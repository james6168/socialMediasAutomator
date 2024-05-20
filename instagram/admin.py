from django.contrib import admin
from .models import Image, HistorySlide, History, Post, Character
from .tasks import create_publication

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']

class HistorySlideAdmin(admin.ModelAdmin):
    list_display = ['image', 'short_text']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published']

    def publish_posts(self, request, queryset):
        for post in queryset:
            create_publication(post.id)
        self.message_user(request, 'Process for posts publication has been started')
    
    publish_posts.short_description = 'Publish selected posts'


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'instagram_username']

admin.site.register(Image, ImageAdmin)
admin.site.register(HistorySlide, HistorySlideAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Character, CharacterAdmin)



