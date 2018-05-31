from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.welcome,name = 'Welcome'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^hotel/',views.hotel,name='Hotel'),
    url(r'^restaurant/(\d+)',views.restaurant,name='Restaurant'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
