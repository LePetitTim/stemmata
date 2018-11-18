from django.db import models

# Create your models here.


class Member(models.Model):
    FEMALE = 'FE'
    MALE = 'MA'
    GENDERS = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    parent_1 = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
    parent_2 = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=1, blank=True, choices=GENDERS,
                              default=FEMALE)
