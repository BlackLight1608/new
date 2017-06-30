from __future__ import unicode_literals
from django.db import models


class File(models.Model):
    file = models.FileField(null=True,blank=True)

    def __str__(self):
        return u'File : %s'%(self.file)


class analyze(models.Model):
    workbk   = models.CharField(max_length=20, blank=True)
    no_sub   = models.CharField(max_length=20, blank=True)
    new_file = models.CharField(max_length=20 , blank=True)
    credit = models.CharField(max_length=20, blank=True)

class update(models.Model):
    workbk   = models.CharField(max_length=20, blank=True)
    reg   = models.CharField(max_length=20, blank=True)
    sub = models.CharField(max_length=20 , blank=True)
    grd = models.CharField(max_length=20, blank=True)
