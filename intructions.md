# ThunderCheck Smart House - IoT Energy Monitoring

## Project Description

**ThunderCheck Smart House** is a compact, intelligent system designed to integrate seamlessly with household appliances. It enables real-time monitoring and control of appliances while providing valuable insights into energy consumption. With the ThunderCheck system, users can track energy usage, control appliances remotely, and receive smart energy-saving recommendations.

---

## Key Features

1. **Universal Appliance Compatibility**
   - ThunderCheck connects to a wide range of household devices, including lamps, fans, kettles, TVs, toasters, and more. It's designed to be plug-and-play for easy integration into any smart home setup.

2. **Real-Time Monitoring of Energy Consumption**
   - Monitor power usage for individual appliances as well as the total energy consumed by the entire home. The system continuously tracks energy usage and sends data to the cloud.

3. **Remote Control via MQTT**
   - Control appliances remotely via MQTT by sending commands to the `iot/devices/commands` topic. You can turn appliances on or off from anywhere.

4. **Smart Energy Recommendations (TO DO)**
   - Based on energy usage patterns, ThunderCheck provides personalized energy-saving tips to optimize consumption.

5. **Automated Alerts and Safety Measures (TO DO)**
   - Receive alerts if an appliance is consuming too much power, indicating potential issues like malfunction or overheating.

6. **Energy Cost Insights and Forecasting (TO DO)**
   - Track your energy costs in real-time and forecast your monthly energy bills based on consumption trends.

7. **Customizable Automation and Scheduling (TO DO)**
   - Set up schedules to automate appliance usage based on your daily routines. For example, program your lights to turn off when you leave or set your coffee maker to start brewing at your wake-up time.

8. **Privacy and Security (TO DO)**
   - All communication between devices and the cloud is encrypted, ensuring secure and private data handling.

---

## Project Setup

Follow these instructions to deploy the **ThunderCheck Smart House** system with MQTT (HiveMQ) and InfluxDB.

### 📦 Prerequisites

Before you begin, make sure you have the following:

1. **Python 3.x** installed on your machine. If not, download it from [python.org](https://www.python.org/downloads/).
2. **MQTT Broker**: We use **HiveMQ** for MQTT communication. Obtain your **HiveMQ credentials** by signing up at [HiveMQ](https://www.hivemq.com/).
3. **InfluxDB**: Set up an **InfluxDB instance** for storing device data. You can use **InfluxDB Cloud** or install it locally.

### 1️⃣ **Install Dependencies**

Install the required Python libraries:

```bash
pip install paho-mqtt influxdb-client
