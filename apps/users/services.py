from typing import Optional

from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.common.services import model_update
from apps.users.models import User


def create_user(*, username: str = None, primary_email: str = None, is_active: bool = False, is_staff: bool = False, **extra_fields) -> User:
    # data cleaning
    if not 'password1' in extra_fields:
        raise ValidationError(_('Please Provide password1 and password2'))

    if extra_fields.get('password1') != extra_fields.get('password2'):
        raise ValidationError(_('Passwords Not Matched'))
    
    password = extra_fields.pop('password1')
    extra_fields.pop('password2')

    groups = None
    user_permissions = None
    if 'groups' in extra_fields:
        groups = extra_fields.pop('groups')
        user_permissions = extra_fields.pop('user_permissions')
    
    # user create conditions
    # Create user
    user = User.objects.create_user(
        username=username,
        primary_email=primary_email, 
        is_active=is_active, 
        is_staff=is_staff, 
        password=password,
        **extra_fields
    )
    user.groups = groups
    user.user_permissions = user_permissions
    return user


@transaction.atomic
def user_update(*, user: User, data) -> User:
    non_side_effect_fields = ["first_name", "last_name"]

    user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user

