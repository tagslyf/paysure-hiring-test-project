from django.contrib import admin

from .models import Payment, Policy


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['external_user_id', 'benefit', 'currency', 'amount', 'timestamp']

    def external_user_id(self, obj):
        return obj.policy.external_user_id

    def benefit(self, obj):
        return obj.policy.benefit

    def currency(self, obj):
        return obj.policy.currency


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['external_user_id', 'benefit', 'currency', 'total_max_amount']
