from django.contrib import admin
from . models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex','height', 'predictions')
admin.site.register(Data, DataAdmin)