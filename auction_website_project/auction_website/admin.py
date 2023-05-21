from django.contrib import admin
from . models import Category, Condition, Item, CustomUser, ItemPhoto

# Register your models here.


admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Item)
admin.site.register(CustomUser)
admin.site.register(ItemPhoto)
