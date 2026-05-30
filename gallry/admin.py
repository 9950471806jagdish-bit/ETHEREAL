from django.contrib import admin
from .models import Profile 
from django.utils.safestring import mark_safe
from .models import Post

class ProfileAdmin(admin.ModelAdmin):
    # This will show the username and an image thumbnail in the admin list view
    list_display = ('userprofile', 'image_thumbnail')
    
    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40" height="40" style="border-radius: 4px; object-fit: cover;" />')
        return "None"
    
    image_thumbnail.short_description = 'Image Preview'

# Register with the custom admin class
admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_image_thumbnail',)
    
    def post_image_thumbnail(self, obj):
        if obj.post_image:
            return mark_safe(f'<img src="{obj.post_image.url}" width="40" height="40" style="border-radius: 4px; object-fit: cover;" />')
        return "None"
    
    post_image_thumbnail.short_description = 'Image Preview'

admin.site.register(Post, PostAdmin)
