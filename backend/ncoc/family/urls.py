from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('api/events', EventViewset)
router.register('api/child', ChildViewset)

app_name = 'api'
urlpatterns = [
    # Your URLs...
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
] + router.urls
