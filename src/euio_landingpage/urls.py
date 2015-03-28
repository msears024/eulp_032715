from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from landingpage.views import (
                        LandingPageView, PrivacyPolicy, TermsOfUse,
                        )

urlpatterns = patterns('',
    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^privacy', PrivacyPolicy.as_view(), name="privacy"),
    url(r'^terms/', TermsOfUse.as_view(), name="terms"),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

print "\n\n\n{}\n\n\n".format(urlpatterns)
