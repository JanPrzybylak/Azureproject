# IoT Integration with HiveMQ and InfluxDB

This guide walks you through setting up a pipeline to handle IoT data using HiveMQ (MQTT) and InfluxDB.

## Step 1: Install Required Libraries

Ensure Python is installed on your system. Then, open a terminal or command prompt and run the following command to install the required Python libraries:

```bash
pip install paho-mqtt influxdb-client pandas
```

---

## Step 2: Set Up InfluxDB

### 1. Sign Up for InfluxDB Cloud
Visit [InfluxDB Cloud](https://cloud2.influxdata.com/) and create an account.

### 2. Create a Bucket
- Navigate to `Load Data` → `Buckets` in the left panel.
- Click the **Create Bucket** button.
- Name the bucket `Iot_data` and set the retention period to **30 days**.

### 3. Get Your API Token
- Go to the **API Tokens** section in the InfluxDB UI.
- Copy the token and keep it safe for use in your Python script.

### 4. Test the Bucket
- Open **Data Explorer**.
- Select the `Iot_data` bucket and confirm its readiness by checking for available data.

---

## Step 3: Set Up HiveMQ (MQTT)

### 1. Sign Up for HiveMQ
Visit [HiveMQ Cloud](https://www.hivemq.com/) and create an account.

### 2. Create a New MQTT Broker
- Once logged in, set up a new MQTT broker using the default settings.

### 3. Note Down MQTT Credentials
- Save the **broker URL**, **username**, and **password** provided during the broker setup.

### 4. Test the Connection
- Use an MQTT client tool (e.g., [MQTT.fx](https://mqttfx.jensd.de/)) to test the connection by sending and receiving sample messages.

---

## Step 4: Download and Modify the Python Script

### 1. Download the Script
Clone the project repository or download the Python file.

### 2. Add Your Credentials
Update the script with your:
- InfluxDB URL
- API Token
- HiveMQ Broker URL
- HiveMQ Username and Password

### 3. Run the Script
Execute the script using the following command:

```bash
python your_script_name.py
```

---

## Step 5: Send Commands via HiveMQ Dashboard

### 1. Login to HiveMQ
Use your account credentials to access the HiveMQ dashboard.

### 2. Send Commands
Publish messages to the topic (e.g., `iot/devices/commands`) in the following format:

```json
{
  "device": "lamp",
  "command": "on"
}
```

### 3. Verify Output
Observe the output and verify the device's state in the script logs.

---

## Additional Notes
- Ensure all credentials are kept secure.
- Verify network connectivity for smooth data transfer.

Feel free to modify and extend the script to fit your specific IoT use case!
