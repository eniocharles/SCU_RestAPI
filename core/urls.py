from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import re_path, path, include
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Sistema de Cadastro de Usuário",
        default_version='v1',
        description="Documentação da API",
        terms_of_service="https://github.com/eniocharles",
        contact=openapi.Contact(email="eletroniccharles@gmail.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,  # Se True, qualquer um pode acessar a documentação
    permission_classes=[permissions.AllowAny],  # Pode exigir autenticação se necessário
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
