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

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response

from models import SensorInfo
from serializer import SensorInfoSerializer
import json
from django.core import serializers
# from django.core import serializers
from django.http import JsonResponse



#from uploads.core.forms import DocumentForm

#New Sensor template
def index(request):
	return render(request, 'index.html')


#adding new sensor
@api_view(['POST' ])
def addSensor(request):
	print 'request receive'
	if request.method == 'POST':
		print ('post request ')
		serializer = SensorInfoSerializer(data=request.POST)
		flag = serializer.is_valid()
		print flag
        if serializer.is_valid():
			print 'data is valid'
			serializer.save()
			return Response(status = status.HTTP_200_OK)
			# return Response(serializer.data, status=status.HTTP_201_CREATED)
		# form = SensorForm(request.POST)
		# sensor = SensorInfo(name =request.POST.get('name'), url = request.POST.get('url') ,
		#  numofparams = request.POST.get('numofparams') , namesofparams = request.POST.get('nameofparams') ,
		#  endpoints = request.POST.get('endpoints'))
		# sensor.save()
		# print "data saved"
		# return HttpResponse('Successful')
		
	print(serializer.errors)
	return Response(data = serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get all sensors info 
@api_view(['GET' ])
def getAllSensors(request):

	objects = SensorInfo.objects.all()
	serializer = SensorInfoSerializer(objects, many=True)
	return Response(data = serializer.data , status = status.HTTP_200_OK)
	# tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)
   	# sensorList = []
	# for elt in objects:
		
	# 	# data = serializers.serialize('json', [ elt, ])
		
	# 	data = {'name': elt.name , 'url': elt.url , 'numofparams' : elt.numofparams, 
	# 	'namesofparams': elt.namesofparams, 'endpoints': elt.endpoints}
	# 	sensorList.append(data)
	# # print(sensorList)
	# json =js.dumps(sensorList)
	# print(json)
	# # data = json, status = status.HTTP_200_OK
	# # return JsonResponse(json)
	# return HttpResponse(serializers.serialize('json', json), content_type="application/json")
	
@api_view(['GET' ])
# Create your views here.
def kafkaProducer(request):
    #if request.method == 'GET':
	print 'calling producer'
	
	kafka = KafkaClient('127.0.0.1:9092')
	producer = SimpleProducer(kafka, async=True)
	group_name = "SensorData"
	# topic_name = request.POST.get('name')
	# url = request.POST.get('url')
	# endpoint = request.POST.get('endpoint')
	# resp = urllib2.urlopen(url+endpoint)
	# data = resp.read()
	topic_name = "test"
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
	# producer.send_messages(topic_name, data)
	producer.stop()
	print "producer worked"
	return Response(status = status.HTTP_200_OK)
	#return HttpResponse('BUZZZER')

@api_view(['GET' ])
def kafkaConsumer(request):
	if request.method == 'GET':
		
		group_name = "SensorData"
		# topic_name = request.POST.get('name')
		topic_name = "test"
		
		kafka = KafkaClient('127.0.0.1:9092')
		consumer = SimpleConsumer(kafka, group_name, topic_name, iter_timeout=1)
		
		print "Created consumer for group: [%s] and topic: [%s]" % (group_name, topic_name)
		print "Waiting for messages..."
		print 'streaming odp'
		data = []
		#data.append(consumer.get_message())
		
		for msg in consumer:
			
		  	print msg.message.value
		  	data.append(msg.message.value)
		 	
		
		resp = js.dumps(data)
		# data = resp , status=status.HTTP_200_OK
		return Response(data = resp, status=200)
	else :
		return Response(status=404)
