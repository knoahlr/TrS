from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    url(r'^', views.tableView.as_view(), name='ByPassindex'),
    url(r'^byPassUpdate/(?P<pk>[0-9]+)', views.byPassUpdate.as_view(success_url=reverse_lazy('ByPassindex')), name='ByPassdata')
]