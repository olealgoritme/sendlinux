import configparser
import subprocess
import logging
import logging.handlers
import socket
import paho.mqtt.client as mqtt
import signal
import sys

# SETTINGS CONFIGURATION FILE
settings_file = 'settings.conf'

def on_connect(client, userdata, flags, rc):
    print("Connected.\nStarting Client loop.")
    client.subscribe(endpoint)
    client.loop()

def on_disconnect(client, userdata,rc=0):
    print("DisConnected.")
    print("Stopping Client loop.")
    client.loop_stop()
    logging.debug("DisConnected result code " + str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subbing to: ", endpoint)
    logging.debug("Subbed to endpoint: " +  endpoint)
    client.loop()

def device_callback(client, userdata, message):
    decoded_msg = str(message.payload.decode('utf-8'))
    arr = ['youtu', 'vimeo', 'twitch'] # match video streams for using with mpv
    if any(c in decoded_msg for c in arr):
        print("Good enough! Found a streamable video")
        subprocess.Popen(['mpv', decoded_msg])
    client.loop()


# Setttings / Config
host = socket.gethostname()
config = configparser.ConfigParser()
config.read(settings_file)

# Debug Logger
_log_file = config['GENERAL']['log_file']
logging.basicConfig(filename=_log_file, filemode="w", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Console handler
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(console)

# Debug Log rotation handler
logrotate_handler = logging.handlers.RotatingFileHandler(_log_file, maxBytes=(1000 * 1000), backupCount=5)
logger.addHandler(logrotate_handler)


# Get GENERAL configuration settings
_cfg = config['GENERAL']
_broker_address = _cfg['broker_host']
_broker_port = _cfg['broker_port']
_username       = _cfg['username']
_password       = _cfg['password']


# Get DEVICE configuration settings
_device = config['android-p30-pro']
_device['uuid'] = _device['device_uuid']
_device['type'] = _device['device_type']
endpoint="device" + "/"+ _device['type'] + "/" + _device['uuid']

# Connection settings
our_hostname = "sendlinux." + host
client = mqtt.Client(our_hostname, clean_session=True)
client.enable_logger(logging)

# Register callback handlers
client.on_connect = on_connect
client.on_disconnet = on_disconnect
client.on_subscribe = on_subscribe
client.message_callback_add(endpoint, device_callback)

# Set broker username/password
client.username_pw_set(username=_username,password=_password)

# Connect
client.connect_async(_broker_address)
print("Connecting to broker: ", _broker_address)
client.loop_forever()

