

from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,permissions
from polls.nocodb_utils_v2 import get_nocodb_data
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
       openapi.Info(
           title="My API",
           default_version='v1',
           description="API documentation for My Django Project",
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
