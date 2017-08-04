from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.tableView.as_view(), name='index'),
    url(r'^$(?P<TRNO>[0-9]+)', views.TrUpdate.as_view(), name='data'),

]