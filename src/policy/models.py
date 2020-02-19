from django.db import models


class Policy(models.Model):
    external_user_id = models.CharField(max_length=255, unique=True)
    benefit = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    total_max_amount = models.FloatField()

    class Meta:
        db_table = 'policy_policy'

    def __str__(self):
        return f'{self.external_user_id} - {self.benefit} {self.currency} {self.total_max_amount:.2f}'


class Payment(models.Model):
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'policy_payment'

    def __str__(self):
        return f'{self.policy.external_user_id}: {self.amount:.2f} {self.timestamp:%Y-%m-%d %H:%M:%S}'
