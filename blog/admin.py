from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'author', 'created_time', 'modified_time', ]

    # 筛选器
    list_filter = ['category', 'title']
    search_fields = ['title', 'body']  # 搜索字段
    date_hierarchy = 'created_time'  # 详细时间分层筛选

    filter_horizontal = ('tags',)

admin.site.site_header = '博客后台'
admin.site.site_title = '博客后台'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
