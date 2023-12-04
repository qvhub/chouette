from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Chouette API",
        default_version="v1",
        description="chouette backend API",
    ),
    public=True,
)

urlpatterns = [
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger",
    ),
    path(
        r"redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/plots/', include('plots.urls')),
]
