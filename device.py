import random
import time
import json
import paho.mqtt.client as mqtt
from influxdb_client_3 import InfluxDBClient3, Point

# InfluxDB 3.x credentials
influx_url = "https://eu-central-1-1.aws.cloud2.influxdata.com"  # Your InfluxDB URL
influx_token = "SM3hB7p6ij3sC8LjvqVC91RhuJZkQKOE_YQtYzbAKQv-hXw9UCL5MqKsYJbYgElY7HaCdjwUbHpv-KUiuss11A=="  # Your API token
influx_org = "IT in English"  # Your organization
influx_bucket = "Iot_data"  # Your bucket name

# Initialize InfluxDB 3.x client
influx_client = InfluxDBClient3(host=influx_url, token=influx_token, org=influx_org)

# HiveMQ MQTT broker details
broker_url = "mqtt-broker-4czymm.a03.euc1.aws.hivemq.cloud"
broker_port = 8883  # TLS port
mqtt_topic = "iot/devices"  # MQTT topic to publish data
command_topic = "iot/devices/commands"  # Topic to receive commands

# MQTT credentials
mqtt_username = "hivemq.webclient.1738068530341"  # Replace with your HiveMQ username
mqtt_password = "N15,4!C9Y*aJP@Vbirhf"  # Replace with your HiveMQ password

# List of possible devices
devices = ["charger", "iron", "kettle", "tv", "lamp", "toaster", "pc"]

# Dictionary to track device states
device_states = {device: "device off" for device in devices}

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(command_topic)  # Subscribe to the command topic
        print(f"Subscribed to topic: {command_topic}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    device = payload.get("device")
    command = payload.get("command")

    if device and command:
        print(f"Received command: {command} for device: {device}")
        if device in device_states:
            if command == "off":
                device_states[device] = "device off"
                print(f"Turning {device} off")
            elif command == "on":
                device_states[device] = "device on"
                print(f"Turning {device} on")
            else:
                print(f"Unknown command: {command}")
        else:
            print(f"Device {device} not found!")
    else:
        print("Invalid message format received!")

# Simulate device data
def simulate_device(client):
    while True:
        # Randomly select a device
        device = random.choice(devices)
        
        # Use the state of the device as stored in the device_states dictionary
        appliance_state = device_states[device]
        energy_consumption = random.uniform(1, 1000) if appliance_state == "device on" else 0
        
        # Create payload
        payload = {
            "device": device,
            "appliance_state": appliance_state,
            "energy_consumption": f"{energy_consumption:.2f} watts",
            "timestamp": time.time()
        }
        
        # Convert payload to JSON
        message = json.dumps(payload)
        
        # Publish to MQTT broker
        result = client.publish(mqtt_topic, message, qos=1)
        
        # Check if the message was published successfully
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Data sent to MQTT Broker: {message}")
        else:
            print(f"Failed to send data to MQTT Broker: {result}")
        
        # Send data to InfluxDB
        send_to_influxdb(device, appliance_state, energy_consumption)
        
        # Wait for 5 seconds before sending the next data
        time.sleep(5)

# Send data to InfluxDB
def send_to_influxdb(device, appliance_state, energy_consumption):
    # Round the energy consumption to an integer if the table expects integers
    energy_consumption_int = int(round(energy_consumption))

    # Create a Point object
    point = Point("iot_measurement") \
        .tag("device", device) \
        .field("appliance_state", appliance_state) \
        .field("energy_consumption", energy_consumption_int)
    
    try:
        # Write the point to InfluxDB
        influx_client.write(record=point, database=influx_bucket)
        print(f"Data sent to InfluxDB: {point.to_line_protocol()}")
    except Exception as e:
        print(f"Failed to send data to InfluxDB: {e}")


# Set up MQTT client
client = mqtt.Client(client_id="iot-device-simulator")
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.tls_set()  # Enable TLS for secure connection

# Assign event callbacks
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

# Connect to the MQTT broker
print("Connecting to MQTT Broker...")
client.connect(broker_url, port=broker_port, keepalive=60)

# Start the MQTT loop
client.loop_start()

# Simulate device data
try:
    simulate_device(client)
except KeyboardInterrupt:
    print("Simulation stopped by user")
finally:
    # Disconnect from the MQTT broker
    client.loop_stop()
    client.disconnect()
    print("Disconnected from MQTT Broker")
