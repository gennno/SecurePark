#include <NewPing.h>
#include <WiFi.h>
#include <FirebaseESP32.h>

// Definisikan pin trigger dan echo untuk masing-masing sensor
#define TRIGGER_PIN1  2
#define ECHO_PIN1     15
#define TRIGGER_PIN2  4
#define ECHO_PIN2     16
#define TRIGGER_PIN3  5
#define ECHO_PIN3     17
#define TRIGGER_PIN4  18
#define ECHO_PIN4     19
#define TRIGGER_PIN5  21
#define ECHO_PIN5     22

// Definisikan jarak maksimal yang akan diukur (dalam mm)
#define MAX_DISTANCE 2000 // Maksimum jarak untuk sensor (dalam mm)

// Definisikan nilai jarak untuk status terisi untuk masing-masing sensor (dalam mm)
#define SENSOR1_THRESHOLD  79
#define SENSOR2_THRESHOLD  85
#define SENSOR3_THRESHOLD  85
#define SENSOR4_THRESHOLD  79
#define SENSOR5_THRESHOLD  73

NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE);
NewPing sonar2(TRIGGER_PIN2, ECHO_PIN2, MAX_DISTANCE);
NewPing sonar3(TRIGGER_PIN3, ECHO_PIN3, MAX_DISTANCE);
NewPing sonar4(TRIGGER_PIN4, ECHO_PIN4, MAX_DISTANCE);
NewPing sonar5(TRIGGER_PIN5, ECHO_PIN5, MAX_DISTANCE);

// WiFi credentials
const char* ssid = "wifi ssid";
const char* password = "123456";

// Firebase credentials
#define FIREBASE_HOST "fierbase5"
#define FIREBASE_AUTH "asdjakehekja"

FirebaseData firebaseData;
FirebaseAuth firebaseAuth;
FirebaseConfig firebaseConfig;

void setup() {
  Serial.begin(115200);
  connectToWiFi();

  // Inisialisasi Firebase
  firebaseConfig.host = FIREBASE_HOST;
  firebaseConfig.signer.tokens.legacy_token = FIREBASE_AUTH;
  Firebase.begin(&firebaseConfig, &firebaseAuth);
  Firebase.reconnectWiFi(true);
}

void loop() {
  delay(1000); // Sedikit jeda untuk menghindari gangguan
  checkSensor(1, sonar1.ping_cm() * 10, SENSOR1_THRESHOLD);
  checkSensor(2, sonar2.ping_cm() * 10, SENSOR2_THRESHOLD);
  checkSensor(3, sonar3.ping_cm() * 10, SENSOR3_THRESHOLD);
  checkSensor(4, sonar4.ping_cm() * 10, SENSOR4_THRESHOLD);
  checkSensor(5, sonar5.ping_cm() * 10, SENSOR5_THRESHOLD);
}

void checkSensor(int sensorID, unsigned int distance, unsigned int threshold) {
  String status;
  if (distance == 0) {
    status = "Tidak terdeteksi";
  } else if (distance <= threshold) { // Membandingkan jarak dengan threshold yang sesuai untuk sensor tertentu
    status = "terisi";
  } else {
    status = "tersedia";
  }
  
  Serial.print("Sensor ");
  Serial.print(sensorID);
  Serial.print(": ");
  Serial.print(distance);
  Serial.print("mm ");
  Serial.println(status);

  // Update status ke Firebase
  String path = "/Slots1_5/" + String(sensorID);
  if (Firebase.setString(firebaseData, path, status)) {
    Serial.println("Update ke Firebase berhasil");
  } else {
    Serial.print("Gagal update ke Firebase: ");
    Serial.println(firebaseData.errorReason());
  }
}

void connectToWiFi() {
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
