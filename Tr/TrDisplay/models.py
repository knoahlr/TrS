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
    Pub_date = forms.DateTimeField(' date published ', widget=forms.TextInput(attrs={'disabled':'True'}))

    class Meta:
        model = TrClass
        #
        fields = '__all__'
        #labels = {'FromTeam':'from team', 'ToTeam':'To team'}
        # fields = ['Tr_NO', 'FromTeam', 'ToTeam', 'Prior_Int', 'Pub_date', 'owner', 'comments']
        # fields['Pub_date'].widget.attrs['readonly'] = True
