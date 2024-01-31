from django.contrib import admin

from .models import Spending


class SpendingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["description"]}),
        (None, {"fields": ["amount"]}),
        (None, {"fields": ["spent_at"]}),
        (None, {"fields": ["currency"]}),
    ]
    list_display = ["description", "amount", "currency", "spent_at"]
    list_filter = ["currency"]
    search_fields = ["description"]


admin.site.register(Spending, SpendingAdmin)
