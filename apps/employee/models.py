from django.db import models
from core.models import BaseModel, Region, District


class Organization(BaseModel):
    name = models.CharField(_('Organization name'), max_length=255)
    region = models.ForeignKey(Region, null=True, related_name='organizations', on_delete=models.SET_NULL)
    district = models.ForeignKey(District, null=True, related_name='organizations', on_delete=models.SET_NULL)


class Department(BaseModel):
    pass


class Employee(BaseModel):
    pass
