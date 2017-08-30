from __future__ import unicode_literals

from django  import forms
from django.db import models
from django.core.urlresolvers import reverse

class ByPassRequest(models.Model):

    ClaimantName = models.CharField(max_length=200, default='Not Assigned')
    Pub_date = models.DateTimeField(' date published ')
    GerritLink = models.CharField(max_length=200)
    CommitNO = models.IntegerField(' Commit NO.')


    def BypassUpdater(self):
        return reverse('ByPassdata', args=[self.CommitNO])



class ByPassForms(forms.ModelForm):
    Pub_date = forms.DateTimeField(' date published ', widget=forms.TextInput(attrs={'disabled':'True'}))

    class Meta:
        model = ByPassRequest
        fields = '__all__'

# Create your models here.
