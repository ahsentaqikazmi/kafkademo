from django.conf.urls import include, url
from django.contrib import admin
import app
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'kafkademo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index, name='index'),
    url(r'^producer/', views.kafkaProducer, name='producer'),
    url(r'^getdata/', views.kafkaConsumer, name='consumer'),
    url(r'^addsensor/', views.addSensor, name='addsensor'),
    url(r'^sensorlist/', views.getAllSensors, name='sensorlist')
    
]
