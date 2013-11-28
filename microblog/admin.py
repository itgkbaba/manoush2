from django.contrib import admin
from models import Note

class NoteOptions(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteOptions)