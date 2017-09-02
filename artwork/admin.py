from django.contrib import admin

from artwork.models import (Category, Type, Artwork)

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Artwork)
