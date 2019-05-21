from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from activity import views
# 正在部署的应用的名称
app_name = '[activity]'

# 定义路由地址
# route=routers.DefaultRouter()

# 注册新的路由地址
# route.register(r'',views.ActivityViewSet)
# route.register(r'activity',views.ActivityViewSet)
# 注册上一级的路由地址并添加
urlpatterns = [
    # url('api/',include(route.urls)),
    url(r'activity/$',views.ActivityView.as_view()),
    url(r'activity/(?P<pk>\d+)/$',views.ActivityDetailView.as_view()),
    url(r'activityplan/$',views.ActivityPlanView.as_view()),
    url(r'activityplan/(?P<pk>\d+)/$',views.ActivityPlanDetailView.as_view()),
    url(r'activitysummary/$',views.ActivitySummary.as_view()),
    url(r'activitysummary/(?P<pk>\d+)/$',views.ActivityDetailSummary.as_view()),
    # url('api/(?P<pk>\d+)/$',include(route.urls))
]
