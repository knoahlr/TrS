from django.shortcuts import render
from django.views.generic import ListView
from .models import ByPassRequest, ByPassForms
from django.views.generic.edit import UpdateView

# def index(request):
#     ByPassRequests = ByPassRequest.objects.all()
#     return render( request, 'ByPass/index.html', context={'ByPassRequests':ByPassRequests})

class tableView(ListView):

    model = ByPassRequest
    template_name = 'ByPass/index.html'

class byPassUpdate(UpdateView):

    form_class = ByPassForms
    model = ByPassRequest
    template_name = 'ByPass/data.html'
    context_object_name = 'BypassObject'
    CommitNO = None

    def get_object(self):

        CommitNO = self.kwargs['pk']
        print(CommitNO)
        BypassQuery = ByPassRequest.objects.filter(CommitNO=CommitNO)
        return BypassQuery.get()