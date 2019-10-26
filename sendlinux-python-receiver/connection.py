import configparser
import subprocess
import logging
import logging.handlers
import socket
import paho.mqtt.client as mqtt


host = socket.gethostname()
config = configparser.ConfigParser()
config.read('settings.conf')

# Logger
_log_file = config['GENERAL']['log_file']
logging.basicConfig(filename=_log_file, filemode="w", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Log rotation handler
logrotate_handler = logging.handlers.RotatingFileHandler(_log_file, maxBytes=(1000 * 1000), backupCount=5)
logger.addHandler(logrotate_handler)

# Console handler
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(console)

# GENERAL configuration settings
_broker_address = config['GENERAL']['broker_host']
_username = config['GENERAL']['username']
_password = config['GENERAL']['password']
_device_uuid = config['android-p30-pro']['device_uuid']
_device_type = config['android-p30-pro']['device_type']

endpoint="device/" + _device_type + "/" + _device_uuid

##############
def on_message(client, userdata, message):
    decoded_msg = str(message.payload.decode("utf-8"))
    if message.topic == endpoint:
       logging.debug("Got this: " + decoded_msg + " from: " + _device_uuid)
       arr = ['youtu', 'vimeo', 'twitch']
       if any(c in decoded_msg for c in arr):
            print("Good enough! Found a streamable video")
            subprocess.run(['mpv', decoded_msg, '--really-quiet'])
#############

client = mqtt.Client("sendlinux" + "." + host)
client.on_message = on_message
client.username_pw_set(username=_username,password=_password)

logging.debug("Connecting to broker: " + _broker_address)
client.connect(_broker_address)

logging.debug("Subbed to endpoint:" + endpoint)
client.subscribe(endpoint)

client.loop_forever()
