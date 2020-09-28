from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Skin Cancer API",
        default_version='v1',
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('', include('dashboard.urls')),
    path('', include('user.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
]
