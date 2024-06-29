from django.contrib import admin
from django.urls import path,include
from rest_framework import routers



from .import views

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'', views.RegistrationViewSet)
urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart_details,name='cart'),
    path('checkout',views.checkout_details,name='checkout'),
    path('order',views.order_detail,name='order'),
     path('restapi/', include(router.urls)),
    
  
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
