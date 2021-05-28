from django.db import models
from django.db.models import SET_NULL


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)
    created_by = models.ForeignKey('users.User', SET_NULL, null=True, blank=True,
                                   related_name='created_%(model_name)ss')
    updated_by = models.ForeignKey('users.User', SET_NULL, null=True, blank=True,
                                   related_name='updated_%(model_name)ss')

    class Meta:
        abstract = True
        ordering = ('id',)


class Country(BaseModel):
    name = models.CharField(_('Country name'), max_length=255)
    code = models.CharField(_('Country code'), max_length=3)


class Region(BaseModel):
    name = models.CharField(_('Region name'), max_length=255)
    country = models.ForeignKey('Country', SET_NULL, null=True, blank=True, related_name='regions')


class District(BaseModel):
    name = models.CharField(_('District name'), max_length=255)
    country = models.ForeignKey('Region', SET_NULL, null=True, blank=True, related_name='districts')
