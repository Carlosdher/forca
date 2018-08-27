# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Palavras(models.Model):
    id = models.AutoField(primary_key=True)
    palavra = models.CharField(max_length=50, verbose_name='palavra')


class Jogada(models.Model):
    Palavra = models.ForeignKey(Palavras, on_delete=models.CASCADE)
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE)
