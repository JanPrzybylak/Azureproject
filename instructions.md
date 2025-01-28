## Step 1: Install Dependencies

To get started, you'll need to install a few dependencies. These include libraries for MQTT and InfluxDB interaction.

Run the following command to install the required packages:

```bash
pip install paho-mqtt influxdb-client
# Instructions for Deploying ThunderCheck Smart House

## Step One:
I registered on the InfluxDB Cloud platform, entered my details, and created my profile.

## Step Two:
I familiarized myself with the panel on the left and clicked on "Load Data." After that, parameters appeared below, and I selected "Buckets."

## Step Three:
A page opened where I saw two Buckets that were created automatically. Then, I clicked on "Create Bucket" because I needed a new Bucket.

## Step Four:
I was prompted to fill in the information to create the Bucket. I named it **"Iot_data"** and left two parameters unchanged: 
- The first parameter "Delete Older Than"
- The second parameter "30 days."

## Step Five:
I saw the Bucket I created, then I entered it and saw a field where I could write SQL commands. On the left, I selected my Bucket.

## Step Six:
I went to the "Load Data" section and saw many parameters. I selected "Python," and instructions appeared on how to do it. On the left, there were step-by-step stages. 
- First, I was greeted by the "Overview" section, which didn't have the necessary information.  
- Then, I clicked the "Next" button and moved to another section called "Install Dependencies," where there were two commands that we entered into the Visual Studio Code terminal.
  - The first command was `pip install influxdb3-python.` After this command, the download started in the terminal.
  - After everything loaded, we entered the second command: `pip install pandas.` After the second command finished loading, we moved to the next step called "Get Token," where we found the command that we added to our script:
    ```bash
    export INFLUXDB_TOKEN=9Hz8VmAi38hmWkXXfW0jVO_iJ1cYU3zBxEiNu78qmX-oMvmVggo5uoBPs1rNxzZCSZRP79Ch4eTb0DQI-deyuQ==
    ```

## Step Seven:
After that, we went to "Data Explorer," where we selected the Bucket **"Iot_data"** in the parameters and chose **"iot_measurement"** in the Measurement parameter. Additional parameters appeared.

## Step Eight:
In the appeared **"Fields"** parameter, we checked the boxes, and then we did the same in the appeared **"Tag Keys"** parameter, where we selected **"device"** and checked all the boxes.

## Step Nine:
On the right, there was a field for SQL commands where we wrote:
```sql
SELECT * FROM "iot_measurement".
