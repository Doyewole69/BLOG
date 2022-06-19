from django.contrib import admin
from .models import Title,Date,PublishedDate,Text,Post
# Register your models here.

admin.site.register(Title)
admin.site.register(Date)
admin.site.register(PublishedDate)
admin.site.register(Text)
admin.site.register(Post)
