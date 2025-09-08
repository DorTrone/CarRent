from django.contrib import admin


from .models import Category, Cars, Clients, Rents

admin.site.register(Category)
admin.site.register(Cars)
admin.site.register(Clients)
admin.site.register(Rents)
