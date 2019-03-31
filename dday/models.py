from django.db import models

from rip_auth.models import RipUser
# Create your models here.
class Dday(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    who = models.ForeignKey(to=RipUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)