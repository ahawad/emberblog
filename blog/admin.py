from django.contrib import admin
from blog.models import Blog
from pagedown.widgets import AdminPagedownWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','post_create_date')
    prepopulated_fields = {'slug':('title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Blog,PostAdmin)
