"""Credit_Card_Fraud_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from User import views as user_view
from Bank import views as bank_view
from Admin import views as admin_view
urlpatterns = [
    url('admin/', admin.site.urls),



    url(r'^base/$',user_view.base,name="base"),
    url(r'^$', user_view.home, name="home"),
    url(r'^user_login/$', user_view.user_login, name="user_login"),
    url(r'^user_register/$', user_view.user_register, name="user_register"),
    url(r'^user_account/$', user_view.user_account, name="user_account"),
    url(r'^user_complaint/$', user_view.user_complaint, name="user_complaint"),
    url(r'^user_transaction/$', user_view.user_transaction, name="user_transaction"),
    url(r'^user_home/$', user_view.user_home, name="user_home"),
    url(r'^receivealert/$', user_view.receivealert, name="receivealert"),

    url(r'^base1/$',bank_view.base1,name="base1"),
    url(r'^bank_login/$', bank_view.bank_login, name="bank_login"),
    url(r'^user_usercarddetails/$', bank_view.user_usercarddetails, name="user_usercarddetails"),
    url(r'^view_complaint/$', bank_view.view_complaint, name="view_complaint"),
    url(r'^bank_home/$', bank_view.bank_home, name="bank_home"),

    url(r'^base2/$', admin_view.base2, name="base2"),
    url(r'^admin_login/$', admin_view.admin_login, name="admin_login"),
    url(r'^admin_home/$', admin_view.admin_home, name="admin_home"),
    url(r'^admin_viewdetails/$', admin_view.admin_viewdetails, name="admin_viewdetails"),
    url(r'^riskalert/(?P<tuser>\d+)$', admin_view.riskalert, name="riskalert"),
    url(r'^riskuser/$', admin_view.riskuser, name="riskuser"),
    url(r'^charts/(?P<chart_type>\w+)', admin_view.charts, name="charts"),

]
