#include <Wire.h>
#include <SparkFun_TMP117.h>
#include <time.h>
TMP117 sensor; 

// Motion LEDs for testing
int detectedLED = 13;
int readyLED = 12;
int waitLED = 11;
int pirPin = 7;  //input pin
int micPin = 3;

//var for Motion Detect
int motionDetected = 0;
int pirValue;

//Mic stuff
const int MIC = 0; //the microphone amplifier output is connected to pin A0
int adc;
int dB, PdB; //the variable that will hold the value read from the microphone each time
int noiseCount = 0;
unsigned long intervalNoise=3000;
unsigned long previousMillisNoise = 0;

//Timing
unsigned long previousMillis = 0; //stores last time temp was updated
const long interval = 60000;  //the interval at which temperature is updated

unsigned long previousMotionMillis = 0;
const long motionInterval = 7000; //interval for motion

void setup() {
//Temp sensor setup--------
  Wire.begin();
  Serial.begin(115200); //start communication at 115200 baud
  Wire.setClock(400000); //set clock speed to fastest for better comm
  if (sensor.begin() == true)
    {
      //do nothing
    }else{
      Serial.println("Error starting");
     while(1);
    }

  //Motion sensor setup-------
  pinMode(detectedLED, OUTPUT);
  pinMode(readyLED, OUTPUT);
  pinMode(waitLED, OUTPUT);

  //Set PIR as Input
  pinMode(pirPin, INPUT);

  //Initial 30 second Delay to stabiliize sensor
  digitalWrite(detectedLED, LOW);
  digitalWrite(readyLED, LOW);
  digitalWrite(waitLED, HIGH);
  delay(5000);
  digitalWrite(readyLED, HIGH);
  digitalWrite(waitLED, LOW);

  // Mic Pin setup
  pinMode(micPin, OUTPUT);
    
}

void loop() {
  
  // set up timing for temp sensor
  unsigned long currentMillis = millis();
   
   // get val from temp sensor
  float tempC = sensor.readTempC();
  
  //get val from motion sensor
  pirValue = digitalRead(pirPin);
  
  //Temperature -------------------------------------------------------------------------
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis; //save the last time temperature was retrieved
    Serial.print("T");
    Serial.println(tempC);
  }

  //Motion Detection---------------------------------------------------------------------
  pirValue = digitalRead(pirPin);
  
  if (pirValue == LOW) {
    previousMotionMillis = millis();
    digitalWrite(detectedLED, LOW);
    digitalWrite(readyLED, HIGH);
  }
  if (pirValue == HIGH){
    digitalWrite(detectedLED,HIGH);
    digitalWrite(readyLED, LOW);
  }
  
  if (pirValue == HIGH && (currentMillis - previousMotionMillis >= motionInterval)){
    previousMotionMillis = currentMillis;
    digitalWrite(detectedLED, HIGH);
    Serial.println("M1");
  }else{
    digitalWrite(detectedLED, LOW);
  }

   //Microphone ---------------------------------------------------------------------
  PdB = dB; //Store the previous of dB here
//  
  adc= analogRead(MIC); //Read the ADC value from amplifer 
//  //Serial.println (adc);//Print ADC for initial calculation 
  dB = (adc - 110.233) / 3.212; //Convert ADC value to dB using Regression values
  if (PdB!=dB);
  //Serial.println(dB);
  //delay(500);
  //Serial.println(noiseCount);
  if (dB>110)
  {
    Serial.println("ALOUD"); //a very loud noise was detected
    //delay(2000);
  }
  if (dB>80)
  { 
    //Serial.println(dB);
  unsigned long currentMillisNoise = millis();
  if ((unsigned long)(currentMillisNoise - previousMillisNoise) >= intervalNoise){
    noiseCount = noiseCount + 1;
    //Serial.println(noiseCount);
    previousMillisNoise = millis();
  }

    if (noiseCount ==10) {
    Serial.println("ACONST"); //a lot of constant noise is happening
    noiseCount = 0;
    previousMillisNoise = millis();
    return;

    }    
 
  } }
