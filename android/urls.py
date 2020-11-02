#viewset으로 만든 url을 맵핑하는 곳

from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path

# router = DefaultRouter()
# router.register(r'talks', views.talkViewSet)
# urlpatterns = [
#     path(r'^',include(router.urls)),
#     path(r'^api-v1/', include('rest_framework.urls', namespace='rest_framework_category'))
# ]

urlpatterns = [
    path('',views.talkViewSet),
]