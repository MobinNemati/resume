
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from resume.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
    path('sitemap.xml/', sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt/', include('robots.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]   

urlpatterns += static(settings.STATIC_URL, ducument_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, ducument_root=settings.MEDIA_ROOT)