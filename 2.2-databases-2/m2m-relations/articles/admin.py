from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = [form.cleaned_data['is_main'] for form in self.forms]
        del_form = [f for f in self.forms if not f.cleaned_data['DELETE']]
        tags = set([form.cleaned_data['tag'] for form in del_form])
        if is_main.count(True) > 1:
            raise ValidationError('Основным может быть один тег')
        if len(tags) != len(del_form):
            raise ValidationError('Обнаружен дубликат тега!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset
    verbose_name = 'Тематика статьи'
    verbose_name_plural = 'Тематики статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['title']
    list_display_links = ['id', 'title']
    inlines = [ScopeInline]
    ordering = ['-published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
