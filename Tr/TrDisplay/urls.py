from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse_lazy


urlpatterns = [

    url(r'^$', views.tableView.as_view(), name='index'),
    url(r'^UpdateTr/(?P<pk>[0-9]+)', views.TrUpdate.as_view(success_url=reverse_lazy('index')), name='data')

]