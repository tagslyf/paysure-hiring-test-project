from django.db.models import Sum
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import Policy, Payment
from .serializers import PaymentSerializer, PolicySerializer


class PolicyViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    model = Policy
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class PaymentViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    model = Payment
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        self.serializer_class(data=data).is_valid(raise_exception=True)

        external_user_id = data['external_user_id']
        benefit = data['benefit']
        currency = data['currency']

        try:
            policy = Policy.objects.get(external_user_id=external_user_id, benefit=benefit, currency=currency)
        except Policy.DoesNotExist:
            return Response({'authorized': False, 'reason': 'POLICY_NOT_FOUND'}, status=200)

        payments = Payment.objects.filter(policy=policy)
        payments_total_amount = payments.aggregate(Sum('amount')).get('amount__sum') or 0

        if payments_total_amount + float(data['amount']) > policy.total_max_amount:
            return Response({'authorized': False, 'reason': 'POLICY_AMOUNT_EXCEEDED'}, status=200)

        payment = Payment.objects.create(policy=policy, amount=data['amount'], timestamp=data['timestamp'])

        return Response({'authorized': True, 'reason': None}, status=200)        
