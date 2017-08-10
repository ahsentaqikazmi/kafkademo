from django.shortcuts import render
#from django.shortcuts import render
from django.http import HttpResponse
from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
from kafka import SimpleConsumer, SimpleClient
from kafka import KafkaConsumer
from kafka import KafkaClient
import pandas as pd
import simplejson as js
import psycopg2
from app.models import SensorInfo
from app.forms import SensorForm
import urllib2
#from uploads.core.forms import DocumentForm

#New Sensor template
def index(request):
	return render(request, 'index.html')
#adding new sensor
def addSensor(request):

	if request.method == 'POST':
		form = SensorForm(request.POST)
		sensor = SensorInfo(name =request.POST.get('name'), url = request.POST.get('url') ,
		 numofparams = request.POST.get('numofparams') , namesofparams = request.POST.get('nameofparams') ,
		 endpoints = request.POST.get('endpoints'))
		sensor.save()
		print "data saved"
		return HttpResponse('Successful')
	return HttpResponse('Failed')

# get all sensors info 
def getAllSensors(request):
	objects = SensorInfo.objects.all()
   	sensorList = []
	for elt in objects:
		
		data = {'name': elt.name , 'url': elt.url , 'numofparams' : elt.numofparams, 
		'namesofparams': elt.namesofparams, 'endpoints': elt.endpoints}
		sensorList.append(data)
	json =js.dumps(sensorList)
	return HttpResponse(json)

# Create your views here.
def kafkaProducer(request):
    #if request.method == 'GET':
	print 'calling producer'
	
	kafka = KafkaClient('127.0.0.1:9092')
	producer = SimpleProducer(kafka, async=True)
	group_name = "SensorData"
	topic_name = "test" #request.POST.get('name')
	#url = request.POST.get('url')
	#endpoint = request.POST.get('endpoint')
	#resp = urllib2.urlopen(url+endpoint)
	#data = resp.read()
	
	#url += endpoint
	#req = urllib.request.Request(url)
	#with urllib.request.urlopen(req) as response:
	#data = response.read()
	
	print "sending messages to group: [%s] and topic: [%s]" % (group_name, topic_name)
	
	#url1 ='https://raw.githubusercontent.com/caroljmcdonald/mapr-streams-sparkstreaming-hbase/master/data/sensordata.csv'
	#data = pd.read_csv(url1)
	#print 'before loop'
	# for i in range(len(data)):    
	#  	print 'msg'
	#  	msg = str(data.iloc[[i]]).split('\n')[1]
	# 	print msg
	#  	producer.send_messages(topic_name, msg)
	#  	print msg + '\n'
	producer.send_messages(topic_name, "this is sensor data1")
	producer.send_messages(topic_name, "this is sensor data2")
	producer.send_messages(topic_name, "this is sensor data3")
	producer.stop()
	print "worked producer"
	return HttpResponse('All Okay')
	#return HttpResponse('BUZZZER')

def kafkaConsumer(request):
	if request.method == 'GET':
		'
		group_name = "my-group"
		topic_name = "test"#request.POST.get('name')
		print 'topic'
		kafka = KafkaClient('127.0.0.1:9092')
		consumer = SimpleConsumer(kafka, group_name, topic_name, iter_timeout=10)
		
		print "Created consumer for group: [%s] and topic: [%s]" % (group_name, topic_name)
		print "Waiting for messages..."
		print 'streaming odp'
		data = []
		#data.append(consumer.get_message())
		
		for msg in consumer:
			
		  	print msg.message.value
		  	data.append(msg.message.value)
		 	
		
		resp = js.dumps(data)
	return HttpResponse(resp)

