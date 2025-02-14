from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.

class BooksInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstatnce(admin.ModelAdmin):
    list_display=('book','status','borrower','due_back','id')
    list_filter=('status','due_back')

    fieldsets = (
        (None, {
            'fields':('book','imprint','id')
        }),
        ('Availability', {
            'fields':('status','due_back','borrower')
        }),
    )

# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)
