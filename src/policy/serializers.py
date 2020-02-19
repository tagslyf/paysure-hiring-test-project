from rest_framework import serializers

from .models import Payment, Policy


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    external_user_id = serializers.CharField(required=True, max_length=255)
    benefit = serializers.CharField(required=True, max_length=255)
    currency = serializers.CharField(required=True, max_length=3)

    class Meta:
        model = Payment
        fields = ('amount', 'timestamp', 'external_user_id', 'benefit', 'currency',)

    def to_representation(self, instance):
        return {
            'external_user_id': instance.policy.external_user_id,
            'benefit': instance.policy.benefit,
            'currency': instance.policy.currency,
            'amount': instance.amount,
            'timestamp': instance.timestamp
        }
