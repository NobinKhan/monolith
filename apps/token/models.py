from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

# Create your models here.


class AccessToken(BaseModel):
    # Choices With enum functionality
    class TokenValidity(models.TextChoices):
        VALID = 'valid', _('Valid')
        INVALID = 'invalid', _('Invalid')
    
    def generate_token():
        return uuid4().hex

    user = models.ForeignKey(get_user_model(), related_name="tokens", on_delete=models.CASCADE, editable=False, null=True, blank=True)
    token = models.UUIDField(default=generate_token, editable=False, null=True, blank=True)
    exp = models.DateTimeField(default=(timezone.now()+timezone.timedelta(hours=24)), editable=False)
    validity = models.CharField(default=TokenValidity.VALID, choices=TokenValidity.choices, max_length=10, blank=True, null=True)


