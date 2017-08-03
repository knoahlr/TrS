from django.shortcuts import render
from django.views.generic import ListView
from .models import TrClass

def index(request):
    Trs = TrClass.objects.all()
    return render(request,'index.html', context={'Trs':Trs})


class tableView(ListView):
    model = TrClass
    template_name = 'index.html'
