#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

// WiFi Parameters
char *path = (char *)malloc(800);
const char* ssid = "The_Admiral";
const char* password = "rollsroyce";
const char* api[] = {"http://pdp-server-2019.herokuapp.com/getPath","https://pdp-server-2019.herokuapp.com/botCont","https://pdp-server-2019.herokuapp.com/endSession"};
int s,i;
int rm1 = D7;
int rm2 = 10;
int lm1 = D5;
int lm2 = D6;
int l,c1,c2,c3,r;
int k;
int tdelay = 1000;
int fdelay = 100;
int r0=D0;
int r1=D1;
int r2=D2;
int r3=D3;
int r4=9;

//char reshortn[30];
//char shortn[30];
//const int sizeb=36;
//char s[6] = {'S','R','S','T','S','L','S','R'};

//char s[sizeb] = {'S','S','T','S','T','S','L','S','L','T','S','T','S','S','R','T','S','R','S','S','T','S','R','S','S','R','S','S','S','S','T'};
//S S H S H S L S L S H S S R S R S S H S R S S R S S S S H

void Stop()
{
  digitalWrite(lm1,0);
  digitalWrite(lm2,0);
  digitalWrite(rm1,0);
  digitalWrite(rm2,0);
}
void forward()
{
  digitalWrite(lm1,1);
  digitalWrite(lm2,0);
  digitalWrite(rm1,1);
  digitalWrite(rm2,0);
}  
void smallright()
{
  digitalWrite(lm1,1);
  digitalWrite(lm2,0);
  digitalWrite(rm1,0);
  digitalWrite(rm2,0);
}
void smallleft()
{
  digitalWrite(lm1,0);
  digitalWrite(lm2,0);
  digitalWrite(rm1,1);
  digitalWrite(rm2,0);
}
void left()
{
  digitalWrite(lm1,0);
  digitalWrite(lm2,1);
  digitalWrite(rm1,1);
  digitalWrite(rm2,0);
}
void right()
{
  digitalWrite(lm1,1);
  digitalWrite(lm2,0);
  digitalWrite(rm1,0);
  digitalWrite(rm2,1);
}
int eosens()
{
    readsens();
    if(((c1+c2+c3)==1)||((c1+c2+c3)==2)||((c1+c2+c3)==0)) 
          return 1;
    else  
          return 0;
}
void readsens()
{
    l = digitalRead(r0);    //r0 = 26
    c1 = digitalRead(r1);
    c2 = digitalRead(r2);
    c3 = digitalRead(r3);
    r = digitalRead(r4);
    // lcd.print(l);
    // lcd.print("--");
    // lcd.print(c1);
    // lcd.print("--");
    // lcd.print(c2);
    // lcd.print("--");
    // lcd.print(c3);
    // lcd.print("--");
    // lcd.print(r);
    Serial.println(l);
    Serial.print(c1);
    Serial.print(c2);
    Serial.print(c3);
    Serial.print(r);
}
void inch()
{
    //lcd.print("Inch function");
    Stop();
    delay(1000);
    forward();
    delay(400);
    Stop();
    delay(1000);
    // lcd.clear();
    readsens();
}
void align()
{
    Stop();
    delay(500);
    forward();
    delay(500);
    // lcd.clear();
    readsens();
}    
// void printing(char prtdirection[])
// {
//     lcd.clear();
//     for(i = 0; prtdirection[i]!='E';i++)
//     {
//         lcd.print(prtdirection[i]);
//     }
//     delay(2000);
// }


void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  pinMode(lm1,OUTPUT);
  pinMode(lm2,OUTPUT);
  pinMode(rm1,OUTPUT);
  pinMode(rm2,OUTPUT);
  pinMode(r0,INPUT);
  pinMode(r1,INPUT);
  pinMode(r2,INPUT);
  pinMode(r3,INPUT);
  pinMode(r4,INPUT);
  // Serial.begin(9600);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
  s=0;
}

void copy(char *a,char *b){
  int k=0;
  while(b[k]!=NULL){
    a[k]=b[k];
    k++;
  }
  a[k]=NULL;
}
void navigate()
{
  readsens();
    if(path[i]=='R')
    {
      inch();
      right();
      delay(tdelay);
      Stop();
    }

    else if(path[i]=='L')
    {
      inch();
      left();
      delay(tdelay);     
      Stop();
    }

    else if(path[i]=='H')
    {
      s=1;
      inch();
      Stop();
      // delay(5000);
      Stop();
    }

    else if(path[i]=='S')
    {
        delay(1000);
        readsens();
        while(!((((l == 0)&&(c1 == 0)&&(c2 == 0)&&(c3 == 0)&&(r == 0)))))
        { 
           
        if (((l == 1)&&(c1 == 0)&&(c2 == 1)&&(c3 == 1)&&(r == 1))||((l == 1)&&(c1 == 0)&&(c2 == 0)&&(c3 == 1)&&(r == 1)))
          {
            // lcd.print("Left");
            smallleft();
          }
        else if (((l == 1)&&(c1 == 1)&&(c2 == 1)&&(c3 == 0)&&(r == 1))||((l == 1)&&(c1 == 1)&&(c2 == 0)&&(c3 == 0)&&(r == 1)))
            {
            // lcd.print("Right");
            smallright();
           }
           else
          {
            // lcd.print("Forward");
            forward();
           }
         readsens();
        }   
    }
    else if(path[i]=='E')
    {
      s=2;
      Stop();
    }
}

void loop() {
  // Check WiFi Status
  if ((WiFi.status() == WL_CONNECTED)&&(s<4)) {
    Serial.println("Issuing GET");
    HTTPClient http;  //Object of class HTTPClient
    http.begin(api[s]);
    int httpCode = http.GET();
//    Serial.println(httpCode);
    //Check the returning code                                                                  
    if (httpCode > 0) {
      const size_t bufferSize = JSON_OBJECT_SIZE(2) + 100;
      DynamicJsonBuffer jsonBuffer(bufferSize);
      JsonObject& root = jsonBuffer.parseObject(http.getString());
      bool ready;
      // Parsing
      if(s==0){
        Serial.println("Case0");
        ready = root["ready"];
        if(ready==1){
            const char* tpath = root["path"];
            int k=0;
            while(tpath[k]!=NULL){
              path[k]=tpath[k];
              k++;
            }
            path[k]=NULL;
            Serial.println(path);
            s=4;
            i=0;
        }
        else
          jsonBuffer.clear();
        
      }
      else if(s==1){
        Serial.println("Case1");
//         const size_t bufferSize2 = JSON_OBJECT_SIZE(1) + 10;
//         DynamicJsonBuffer jsonBuffer(bufferSize2);
//         JsonObject& root = jsonBuffer.parseObject(http.getString());
        ready = root["S"];
        if(ready==1){
          Serial.println(ready);
          s=4;
        }
      }
      else if(s==2){
        Serial.println("Stop");
        s=0;
    }
    }
    http.end();   //Close connection
    delay(200);
  }
  else{
    navigate();
    i++;
  }
  // Delay
}
