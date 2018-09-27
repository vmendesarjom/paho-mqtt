import paho.mqtt.client as mqtt
'''
#testes
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    op = input
    while True:
        if op != 'sair':
            client.publish("D1", op)
            op = input
        else:
            client.loop_stop()

#
def on_disconnect(client, userdata,rc):
    if rc != 0:
        logging.debug("DisConnected result code "+str(rc))
        client.loop_stop()
#

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

client.connect("localhost", 1883, 60)

client.loop(.1)
'''

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    op = input
    while (op != "sair"):
        client.publish("D1", op)
        op = input

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
