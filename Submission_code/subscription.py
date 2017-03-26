import paho.mqtt.client as mqtt

def on_message(client,userdata,msg):
    f = open("data.txt","w")
    print msg.payload
    f.write(msg.payload)


client = mqtt.Client()
client.on_message = on_message
client.connect("127.0.0.1",1883)
client.subscribe("touch")
client.loop_forever()
