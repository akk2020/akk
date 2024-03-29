"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.urls import path
from demo import views
from django.contrib.auth import login, logout


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),

# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    # url(r'^login/$', views.account_login, name='login'),
    url(r'^$', views.account_login, name='login'),
    # url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
    url(r'^$', views.account_login, name='logout'), #login画面に戻る
]
