from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

# Create your models here.

class Email(BaseModel):
    email = models.EmailField(_('Email'), unique=True, null=True, blank=True)
    role = models.CharField(verbose_name=_('Role'), max_length=30, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["role", 'email'],
                name="unique_email_address"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.email}"
