import random
import time
import json
import paho.mqtt.client as mqtt

# HiveMQ Broker Details
broker_url = "mqtt-broker-4czymm.a03.euc1.aws.hivemq.cloud"
broker_port = 8883  # TLS port
mqtt_username = "hivemq.webclient.1738068530341"  # Replace with your HiveMQ username
mqtt_password = "N15,4!C9Y*aJP@Vbirhf"  # Replace with your HiveMQ password

# List of possible devices
devices = ["charger", "iron", "kettle", "tv", "lamp", "toaster", "pc"]

# Store the state of devices (on/off)
device_states = {device: "off" for device in devices}

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HiveMQ Broker!")
        # Subscribe to the commands topic
        client.subscribe("iot/devices/commands")
        print("Subscribed to topic: iot/devices/commands")
    else:
        print(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")

def on_message(client, userdata, msg):
    print(f"Received message from topic {msg.topic}: {msg.payload.decode()}")
    try:
        # Decode JSON payload
        payload = json.loads(msg.payload)
        device = payload.get("device")
        command = payload.get("command")

        # Handle commands
        if device in device_states:
            if command == "off":
                print(f"Turning {device} off")
                device_states[device] = "off"
            elif command == "on":
                print(f"Turning {device} on")
                device_states[device] = "on"
            else:
                print(f"Unknown command: {command} for device: {device}")
        else:
            print(f"Device {device} not found.")
    except Exception as e:
        print(f"Error processing message: {e}")

# Simulate device data
def simulate_device(client):
    while True:
        device = random.choice(devices)
        appliance_state = device_states[device]
        energy_consumption = random.uniform(1, 1000) if appliance_state == "on" else 0
        
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
        result = client.publish("iot/devices", message, qos=1)
        
        # Check if the message was published successfully
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Data sent to MQTT Broker: {message}")
        else:
            print(f"Failed to send data to MQTT Broker: {result}")
        
        # Wait for 5 seconds before sending the next data
        time.sleep(5)

# Set up MQTT client
client = mqtt.Client(client_id="iot-device-simulator")
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.tls_set()  # Enable TLS for secure connection

# Assign event callbacks
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

# Connect to the HiveMQ Broker
print("Connecting to HiveMQ Broker...")
client.connect(broker_url, broker_port, keepalive=60)

# Start the MQTT loop to listen for incoming messages
client.loop_start()

# Start simulating device data
try:
    simulate_device(client)
except KeyboardInterrupt:
    print("Simulation stopped by user")
finally:
    # Disconnect from the MQTT broker
    client.loop_stop()
    client.disconnect()
    print("Disconnected from HiveMQ Broker")
