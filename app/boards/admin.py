from django.contrib import admin
from boards.models import BoardButton

# Register your models here.
class BoardButtonAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "button_label", "button_text"]

admin.site.register(BoardButton, BoardButtonAdmin)