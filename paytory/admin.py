from django.contrib import admin
from .models import Expense, Income, Token

# Register your models here.

class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Display user and created date
    exclude = ('token',)  # Exclude the token from the admin form

    def has_change_permission(self, request, obj=None):
        return False  # Disable change permissions

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token, TokenAdmin)
