from django.contrib import admin
from celleng.models import Ceo, Group
# Register your models here.

class Songkok(admin.ModelAdmin):
    list_display = ['member', 'penulis', 'alamat','status']
    search_fields = ['member', 'penulis', 'alamat','status']

admin.site.register(Ceo)
admin.site.register(Group)