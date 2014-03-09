from django.contrib import admin
from models import Clone


class CloneAdmin(admin.ModelAdmin):
    list_display = ("name", "get_accessions")


admin.site.register(Clone, CloneAdmin)
