#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define SERIAL_DEBUG false
#define BUILTIN_LED 2
#define BUF_SZ 25

// WiFi
const char *ssid = "IDEAPAD-S145-JM";
const char *password = "048Ke34^";

// Localhost MQTT Broker
const char *mqtt_broker = "192.168.137.1";
const char *mqtt_username = "";
const char *mqtt_password = "";
const int mqtt_port = 1883;

const char *sender_topic = "crane_controller/channel1";
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

boolean wifi_connected() {
  return WiFi.status() == WL_CONNECTED;
}

void connect_to_wifi() {
  while (!wifi_connected()) {
    blink_builtin_led(1000);
    if (SERIAL_DEBUG) {
      Serial.println("Connecting to WiFi...");
    }
  }

  if (SERIAL_DEBUG) {
    Serial.println("Connected to the WiFi network");
  }
}

boolean mqtt_connected() {
  return client.connected();
}

void connect_to_mqtt() {
  while (!mqtt_connected()) {
    String client_id = "esp8266-client-";
    client_id += String(WiFi.macAddress());

    if (SERIAL_DEBUG) {
      Serial.printf("Attempting to connect to %s:%d\n", mqtt_broker, mqtt_port);
    }

    if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
      if(SERIAL_DEBUG) {
        Serial.printf("%s connected to %s:%d\n", client_id.c_str(), mqtt_broker, mqtt_port);
      }
      break;
    }

    if (SERIAL_DEBUG) {
      Serial.printf("Could not connect to %s:%d\n", mqtt_broker, mqtt_port);
    }

    blink_builtin_led(2000);
  }

  client.subscribe(receiver_topic);
}

void serial_loop() {
  static char buf[BUF_SZ];
  static int i = 0;

  if (Serial.available()) {
    char c = (char) Serial.read();
    buf[i++] = c;
  }

  if (i == BUF_SZ - 1 || (i > 0 && buf[i - 1] == '\n')) {
    buf[i] = '\0';
    client.publish(sender_topic, buf);
    i = 0;
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);
  digitalWrite(BUILTIN_LED, LOW);

  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  connect_to_wifi();
  
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  connect_to_mqtt();

  digitalWrite(BUILTIN_LED, HIGH);
}

void loop() {
  if (!wifi_connected()) {
    connect_to_wifi();
  }

  if(wifi_connected() && !mqtt_connected()) {
    connect_to_mqtt();
  }

  client.loop();

  serial_loop();
}
