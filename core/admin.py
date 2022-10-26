from django.contrib import admin
from .models import Advocate,Company,Link
import nested_admin
# Register your models here.
class LinkInline(admin.StackedInline):
    model = Link

class AdvocateAdmin(admin.ModelAdmin):
    inlines = [LinkInline]

    class Meta:
        model = Advocate

admin.site.register(Advocate,AdvocateAdmin)
admin.site.register(Company)