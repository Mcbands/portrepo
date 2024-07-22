from django.contrib import admin
from django.urls import path, include
from portfolio.views import Index, Contact, Products, About, Faq, Terms,Services
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Index.as_view(), name="index"),
    path("faq/", Faq.as_view(), name="faq"),
    path("about/", About.as_view(), name="about"),
    path("services/", Services.as_view(), name="services"),
    path("products/", Products.as_view(), name="products"),
    path("contact/", Contact.as_view(), name="contact"),
    path("terms/", Terms.as_view(), name="terms"),
    path("portfolio/", include("portfolio.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
