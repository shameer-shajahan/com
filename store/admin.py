from django.contrib import admin

# Register your models here.

from.models import Tag,Brand,BaseModel,Size,Category,Product

from store.models import User

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(BaseModel)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)