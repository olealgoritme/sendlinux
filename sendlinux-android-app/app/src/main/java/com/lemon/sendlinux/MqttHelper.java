package com.lemon.sendlinux;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttHelper {


    public void send(byte[] msgBuf, String UUID) {
        String endpoint     = "device/android/" + UUID;
        int qos             = 2;
        String broker       = "tcp://vmspinup.no:1883";
        String clientId     = "android-client-" + UUID;
        MemoryPersistence persistence = new MemoryPersistence();

        MqttConnectOptions connOpts = new MqttConnectOptions();
        connOpts.setCleanSession(true);
        connOpts.setUserName("sendlinux");
        connOpts.setPassword("zF_LFK34240F_FFJUkKKK".toCharArray());

        try {
            MqttClient mqttClient = new MqttClient(broker, clientId, persistence);
            mqttClient.connect(connOpts);

            MqttMessage message = new MqttMessage(msgBuf);
            message.setQos(qos);

            mqttClient.publish(endpoint, message);
            mqttClient.disconnect();

        } catch(MqttException me) {
            me.printStackTrace();
        }

    }
}
