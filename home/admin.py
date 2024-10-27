from django.contrib import admin
from .models import Case, ContactMessage, VolunteersEntry

admin.site.register(Case)
admin.site.register(ContactMessage)
admin.site.register(VolunteersEntry)