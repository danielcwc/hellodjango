from django.contrib import admin
from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    # Options for change list:
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    # This ordering overrides the ordering defined in models
    ordering = ('-publication_date',)

    # Options for edit form:
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # Multi-selection box for ManyToMany Fields
    filter_horizontal = ('authors',)
    # To make drop-down select box an text input
    raw_id_fields = ('publisher',)

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)