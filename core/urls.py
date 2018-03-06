from django.conf.urls import url, include
from django.urls import path

from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('deals/', views.deals, name='deals'),
]
