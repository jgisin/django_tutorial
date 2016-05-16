from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ["title","content", "updated", "timestamp"]
  list_display_links = ["title"]
  list_filter = ["updated", "timestamp"]
  list_editable = ["content"]
  search_fields = ["title", "content"]

  class Meta:
    model = Post

admin.site.register(Post, PostAdmin)
