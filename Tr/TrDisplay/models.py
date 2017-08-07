from __future__ import unicode_literals

from django.db import models
from django  import forms
from django.core.urlresolvers import reverse

# Create your models here.
class TrClass(models.Model):

    Tr_NO = models.IntegerField('TR Number')
    FromTeam = models.CharField(max_length=200, default='FromTeam')
    ToTeam = models.CharField(max_length=200, default = 'ToTeam')
    Prior_Int = models.IntegerField('Priority', default = 0)
    Pub_date = models.DateTimeField(' date published ')
    owner = models.CharField(max_length=200, default='Not assigned')
    comments = models.CharField(max_length=200, default = 'Comments')


    def TrUpdater(self):
        return reverse('data', args=[self.Tr_NO])


class TrForms(forms.ModelForm):
    class Meta:
        model = TrClass
        widget = forms.TextInput(attrs={'class': 'special'})
        fields = '__all__'
        labels = {'FromTeam':'from team', 'ToTeam':'To team'}
