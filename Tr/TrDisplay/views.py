from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import TrClass

# def index(request):
#     Trs = TrClass.objects.all()
#     return render(request,'index.html', context={'Trs':Trs})

# def data
class tableView(ListView):
    model = TrClass
    template_name = 'index.html'

class TrUpdate(UpdateView):
    model = TrClass
    template_name = 'data.html'
    fields = ['Prior_Int', 'owner', 'comments' ]

