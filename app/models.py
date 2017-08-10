from django.db import models

# import psycopg2


# Create your models here.
class SensorInfo(models.Model):
    name = models.CharField(max_length = 50)
    url = models.CharField(max_length = 50)
    numofparams = models.IntegerField()
    namesofparams = models.CharField(max_length = 50)
    endpoints = models.CharField(max_length = 50)

    class Meta:
   
      db_table = "sensorinfo"

    # def connectDb(DB):
    #     con = psycopg2.connect(database="ckan_default", user="ckan_default", password="smat")
    #     print 'Connection established'
    #     return con
    
    # def createTable(con):
    #     cur = con.cursor()
    #     cur.execute('''CREATE TABLE sensorinfo
    #     (id INT PRIMARY KEY     NOT NULL,
    #     name           TEXT    NOT NULL,
    #     url            TEXT     NOT NULL,
    #     endpoints      TEXT     NOT NULL,
    #     num_params        TEXT,
    #     params_names         REAL);''')
    #     print "Table created successfully"
    #     con.commit()
        