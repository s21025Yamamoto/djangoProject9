from django.contrib import admin

from .models import Category, OgiriPost

class CategoryAdmin(admin.ModelAdmin):
    '''
    管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')


class OgiriPostAdmin(admin.ModelAdmin):
    '''
    管理ページのレコード一覧に表示するカラムを設定するクラス
    '''

    list_display = ('id', 'title')

    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(OgiriPost, OgiriPostAdmin)

