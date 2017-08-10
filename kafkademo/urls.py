from django.conf.urls import include, url
from django.contrib import admin
import app
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'kafkademo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index, name='index'), # renders form for adding sensor info
    url(r'^producer/', views.kafkaProducer, name='producer'),# send name, url, endpoint as a request to get data from sensor to pipeline
    url(r'^getdata/', views.kafkaConsumer, name='consumer'),# send name as request and get the data from pipeline to u.i
    url(r'^addsensor/', views.addSensor, name='addsensor'),# post request on form submission to add sensor info
    url(r'^sensorlist/', views.getAllSensors, name='sensorlist')# gets all info of all the sensors in db
    
]
