from django.contrib import admin
from models import Clone


class CloneAdmin(admin.ModelAdmin):
    list_display = ("name", "accessions")


admin.site.register(Clone, CloneAdmin)
