#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define SERIAL_DEBUG false
#define BUILTIN_LED 2

// WiFi
const char *ssid = "IDEAPAD-S145-JM";
const char *password = "048Ke34^";

// Online Test MQTT Broker
// const char *mqtt_broker = "broker.emqx.io";
// const char *mqtt_username = "emqx";
// const char *mqtt_password = "public";
// const int mqtt_port = 1883;

// Localhost MQTT Broker
const char *mqtt_broker = "192.168.137.1";
const char *mqtt_username = "";
const char *mqtt_password = "";
const int mqtt_port = 1883;

const char *sender_topic="crane_controller/channel1";
const char *receiver_topic = "crane_controller/channel2";

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char *topic, byte *payload, unsigned int length) {
  if (SERIAL_DEBUG) {
    Serial.print("Message arrived in topic: ");
  }

  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char) payload[i]);
  }

  Serial.print('\n');
}

void blink_builtin_led(int ms) {
  digitalWrite(BUILTIN_LED, HIGH);
  delay(ms);
  digitalWrite(BUILTIN_LED, LOW);
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);
  digitalWrite(BUILTIN_LED, LOW);

  Serial.begin(115200);
  
  // connecting to a WiFi network
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    blink_builtin_led(1000);
    if (SERIAL_DEBUG) {
      Serial.println("Connecting to WiFi...");
    }
  }
  
  if (SERIAL_DEBUG) {
    Serial.println("Connected to the WiFi network");
  }
  
  //connecting to a mqtt broker
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  
  while (!client.connected()) {
    String client_id = "esp8266-client-";
    client_id += String(WiFi.macAddress());

    if (SERIAL_DEBUG) {
      Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
    }

    boolean connected = client.connect(client_id.c_str(), mqtt_username, mqtt_password);

    if (connected) {
      if(SERIAL_DEBUG) {
        Serial.println("Public emqx mqtt broker connected");
      }
      break;
    }

    if (SERIAL_DEBUG) {
      Serial.print("failed with state ");
      Serial.print(client.state());
    }

    blink_builtin_led(2000);
  }

  client.subscribe(receiver_topic);

  digitalWrite(BUILTIN_LED, HIGH);
}

void loop() {
  client.loop();

  const char buf_sz = 25;
  static char buf[buf_sz];
  static int i = 0;

  if (Serial.available()) {
    char c = (char) Serial.read();
    buf[i++] = c;
  }

  if (i >= buf_sz || (i > 0 && buf[i - 1] == '\n')) {
    buf[i] = '\0';
    client.publish(sender_topic, buf);
    i = 0;
  }
}
