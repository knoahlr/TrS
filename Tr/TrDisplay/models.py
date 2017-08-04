from __future__ import unicode_literals

from django.db import models
from django  import forms

# Create your models here.
class TrClass(models.Model):

    Tr_NO = models.IntegerField('TR Number')
    FromTeam = models.CharField(max_length=200, default = 'FromTeam')
    ToTeam = models.CharField(max_length=200, default = 'ToTeam')
    Prior_Int = models.IntegerField('Priority')
    Pub_date = models.DateTimeField(' date published ')
    owner = models.CharField(max_length=200, default='Not assigned')
    comments = models.CharField(max_length=200, default = 'Comments')

class TrForms(forms.ModelForm):
    model = TrClass
    fields = ['Prior_Int', 'owner', 'comments' ]