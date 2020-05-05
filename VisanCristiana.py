import time
import json
import paho.mqtt.client as mqttClient
from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
def on_connect(client, userdata, flags, rc):
  if rc==0:
    print("Connected to broker")
    global Connected
    Connected=True
  else:
    print("Connection failed")
Connected=False
broker_address="mqtt.beia-telemetrie.ro"
port=1883
user=""
password=""
client=mqttClient.Client("Python")
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker_address, port=port)
client.loop_start()
while Connected!=True:
  time.sleep(0.1)
try:
  while True:
    temp=sense.get_temperature()
		print(temp)
		umiditate=sense.get_humidity()
		print(umiditate)
		presiune=sense.get_pressure()
		print(presiune)
    payload_dict={"TEMPERATURE" : temp,
                  "HUMIDITY": umiditate,
                  "PRESSURE": presiune}
    client.publish{"training/rpi/cristiana-visan",json.dumps(payload_dict)}
    time.sleep(10)
except KeyboardInterrupt:
  client.disconnect()
  client.loop_stop()
