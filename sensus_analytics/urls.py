"""sensus_analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import  static
from analytics.views import dashboard,second_view,show_electric_meter,show_water_meter,show_gas_meter,customer_overview
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',dashboard),
    url(r'^overview/',second_view),
    url(r'^overview_gas/',show_gas_meter),
    url(r'^overview_water/',show_water_meter),
    url(r'^overview_electric/',show_electric_meter),
    url(r'^customer_overview/(?P<pk>[0-9]*)[/]*$',customer_overview),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)