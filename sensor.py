#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time, threading, ssl, random
from final_lane_detection import lane_detection
import obd
# client, user and device details
serverUrl   = "absherthon-team-3.iot.gov.sa"
clientId    = "my_mqtt_python_client"
device_name = "test1"
tenant      = "t2764515"
username    = "BilalYussef"
password    = "1416Belal"

receivedMessages = []

# display all incoming messages
def on_message(client, userdata, message):
    print("Received operation " + str(message.payload))
    if (message.payload.startswith("510")):
        print("Simulating device restart...")
        publish("s/us", "501,c8y_Restart");
        print("...restarting...")
 #       time.sleep(1)        publish("s/us", "503,c8y_Restart");
        print("...done...")

# send temperature measurement
def sendMeasurements(np_image):
    try:
        print("Done")
	#lane_detection.find_car_dev(np_image)
        publish("s/us", "211," + str("10")))
    except (KeyboardInterrupt, SystemExit):
        print("Received keyboard interrupt, quitting ...")

# publish a message
#def publish(topic, message, waitForAck = False):
#    mid = client.publish(topic, message, 2)[1]
  #  if (waitForAck):
 #       while mid not in receivedMessages:
#            time.sleep(0.25)

def on_publish(client, userdata, mid):
    receivedMessages.append(mid)

# connect the client to Cumulocity IoT and register a device
client = mqtt.Client(clientId)
client.username_pw_set(tenant + "/" + username, password)
client.on_message = on_message
client.on_publish = on_publish

client.connect(serverUrl)
client.loop_start()
publish("s/us", "100," + device_name + ",c8y_MQTTDevice", True)
publish("s/us", "110,S123456789,MQTT test model,Rev0.1")
publish("s/us", "114,c8y_Restart")
print("Device registered successfully!")

###############
connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
print(response.value.to("mph")) # user-friendly unit conversions
##################
client.subscribe("s/ds")
cap = 
while True:
	sendMeasurements()

	time.sleep(2)

