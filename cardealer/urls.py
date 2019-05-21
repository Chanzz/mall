from cardealer import views
from django.conf.urls import include,url
app_name = '[cardealer]'
urlpatterns = [
    # url('api/',include(route.urls)),
    url(r'cardealer/$',views.CardealerView.as_view()),
    url(r'cardealer/(?P<pk>\d+)/$',views.CardealerDetailView.as_view()),
]