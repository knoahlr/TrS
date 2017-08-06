from django.shortcuts import render
from django.views.generic import ListView
from .models import TrClass, TrForms

from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

def index(request):
    Trs = TrClass.objects.all()
    return render(request,'index.html', context={'Trs':Trs})


class tableView(ListView):

    model = TrClass
    template_name = 'index.html'

class TrUpdate(UpdateView):
    
    form_class = TrForms
    model = TrClass
    TrNO = None
    template_name = 'data.html'
    #fields = ['Prior_Int', 'owner', 'comments' ]
    context_object_name = 'TrObject'
    
    def get_object(self):

        TrNO = self.kwargs['pk']
        TrQuery = TrClass.objects.filter(Tr_NO=TrNO)
        return TrQuery.get()

    # def post(self, request, **kwargs):

    #     request.POST = request.POST.copy()
    #     print(request.POST)
    #     print(self.kwargs)
    #     return super(TrUpdate, self).post(request, **kwargs)


