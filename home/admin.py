from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')
    search_fields = ('user',)
    list_filter = ('updated',)
    raw_id_fields = ('user',)

# admin.site.register(Note, NoteAdmin)
