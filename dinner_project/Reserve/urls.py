from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.welcome,name = 'Welcome'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^hotel/',views.hotel,name='Hotel'),
    url(r'^restaurant/(\d+)',views.restaurant,name='Rest'),
    url(r'^info/(\d+)',views.add,name='Add'),
    url(r'^image/(\d+)',views.image,name='Image'),
    url(r'^menu/(\d+)',views.menu,name='Menu'),
    url(r'^customer/(\d+)',views.customer,name='Customer'),
    url(r'^make/(\d+)',views.make,name='Make'),
    url(r'^moreinfo/(\d+)',views.moreinfo,name='MoreInfo'),
    url(r'^food',views.food,name='Food')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
