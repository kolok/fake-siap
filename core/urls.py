from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

from django.views.generic import TemplateView
import django_cas_ng.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "operations/",
        include(("operations.urls", "operations"), namespace="operations"),
    ),
    path("", include(("users.urls", "users"), namespace="users")),
    path(
        "accounts/cerbere-login",
        django_cas_ng.views.LoginView.as_view(),
        name="cas_ng_login",
    ),
    path(
        "accounts/cerbere-logout",
        django_cas_ng.views.LogoutView.as_view(),
        name="cas_ng_logout",
    ),
    path("cgu", TemplateView.as_view(template_name="editorial/cgu.html"), name="cgu"),
    path(
        "accessibilite",
        TemplateView.as_view(template_name="editorial/accessibilite.html"),
        name="accessibilite",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
