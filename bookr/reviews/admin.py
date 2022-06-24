from django.contrib import admin

from reviews.models import Book, Contributor, BookContributor, Publisher, Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13', 'get_publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date',)
    date_hierarchy = 'publication_date'
    search_fields = ('title', 'isbn', 'publisher__name') #__startswith, __exact

    def get_publisher(self, obj):
        return obj.publisher.name


class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    #fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('creator', 'book')}), ('Review content', {'fields': ('content', 'rating')}))


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names',)
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(BookContributor)
admin.site.register(Publisher)
admin.site.register(Review, ReviewAdmin)
