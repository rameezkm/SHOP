from django.contrib import admin
from . models import Cool, Hot

class CoolAdmin (admin.ModelAdmin):
    list_display=('name','address','gender','phone')
admin.site.register(Cool,CoolAdmin)    
class HotAdmin (admin.ModelAdmin):
    list_display=('product','prize','desc','image')
admin.site.register(Hot,HotAdmin)