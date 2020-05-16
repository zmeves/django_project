from django.contrib import admin
from blogging.models import Post, Category


class CatInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CatInline, ]


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    exclude = ('posts',)

