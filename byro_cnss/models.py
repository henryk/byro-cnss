from annoying.fields import AutoOneToOneField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CNSSProfile(models.Model):
    form_title = _("CNSS profile")

    member = AutoOneToOneField(
        to='members.Member',
        on_delete=models.CASCADE,
        related_name='profile_cnss',
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )
    occupation = models.CharField(
        max_length=511,
        null=True,
        blank=True,
        verbose_name=_('Occupation'),
    )
    occupational_history = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Occupational history'),
    )
