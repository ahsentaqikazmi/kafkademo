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
import urllib.request
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
	topic_name = request.POST.get('name')
	url = request.POST.get('url')
	endpoint = request.POST.get('endpoint')
	url += endpoint
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
	data = response.read()
	print "sending messages to group: [%s] and topic: [%s]" % (group_name, topic_name)
	
	# url ='https://raw.githubusercontent.com/caroljmcdonald/mapr-streams-sparkstreaming-hbase/master/data/sensordata.csv'
	data = pd.read_csv(url)
	#for i in range(len(data)):    
	#	msg = str(data.iloc[[i]]).split('\n')[1]
	producer.send_messages(topic_name, data)
	#	print msg + '\n'
	producer.stop()
	print "worked producer"
	return HttpResponse('All Okay')
	# return HttpResponse('BUZZZER')

def kafkaConsumer(request):
	if request.method == 'GET':
		print 'SOHAIBBBB'
		group_name = "my-group"
		topic_name = "fast-messages"
		print 'topic'
		kafka = KafkaClient('127.0.0.1:9092')
		consumer = SimpleConsumer(kafka, group_name, topic_name)
		print 'consuler'
		print "Created consumer for group: [%s] and topic: [%s]" % (group_name, topic_name)
		print "Waiting for messages..."
		print 'streaming odp'
		for msg in consumer:
			# time.sleep(5)
			print msg.message.value
			#return HttpResponse(msg.message.value)
	return HttpResponse('Consumer nahi chal raha')

