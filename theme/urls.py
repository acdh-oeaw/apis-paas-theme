from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from . import dal_views

app_name = 'theme'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="start"),
    url(r'^imprint/$', views.ImprintView.as_view(), name='imprint'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^expert-search/$', views.PersonListView.as_view(), name='expert-search'),
    url(
        r'^person/(?P<pk>[0-9]+)$',
        views.PersonDetailView.as_view(),
        name='person-detail'
    ),
    url(
        r'^ac/obel-person/$', dal_views.OeblPersons.as_view(),
        name='obel-person-autocomplete',
    ),
]
