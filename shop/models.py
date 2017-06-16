# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Store(models.Model):


    store_name = models.CharField(max_length=70)
    store_type = models.CharField(max_length=40,  default='General' )
    store_logo = models.CharField(max_length=500, default='null')
    store_link = models.CharField(max_length=120)



    def __str__(self):
        return self.store_name

