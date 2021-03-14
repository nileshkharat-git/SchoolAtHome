from django.contrib import admin
from .models import Accounts

class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']


admin.site.register(Accounts,AccountAdmin)

