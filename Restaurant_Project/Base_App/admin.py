from django.contrib import admin
from Base_App .models import ItemList, Items, AboutUs, BookTable

# Register your models here.

admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(BookTable)