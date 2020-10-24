from django.contrib import admin
from.models import *

#customize django admin

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'added_date','image')
    list_editable = ('added_date',) #things to make editable without oprn thme
    list_per_page = 4     #pagenation
    search_fields = ('title',)    #search bar enable in admin
    list_filter = ('cat',)       #make filterable  according to category





# Register your models here.
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)


