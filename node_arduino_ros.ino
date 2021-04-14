#include <ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/Bool.h>

ros::NodeHandle  nh;
std_msgs::Bool bool_msg;
std_msgs::Int8 int_msg;
const long A=100; //resistencia en oscuridad en KΩ
const int B = 15;        //Resistencia a la luz (10 Lux) en KΩ
const int Rc = 10;       //Resistencia calibracion en KΩ
const int LDRPin = A0;   //Pin del LDR

int V;
int ilum;

void incoming(const std_msgs::Int8& toggle_msg){
  int in=toggle_msg.data;
  int pwm=in*14.16;
  analogWrite(9,pwm);
}

ros::Subscriber<std_msgs::Int8> sub("chatterH", incoming);
ros::Publisher chatter("Arduinob", &bool_msg);
ros::Publisher chatteri("Arduinoi", &int_msg);

void setup() {
  // put your setup code here, to run once:
  pinMode(9,OUTPUT);
  pinMode(8,INPUT);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
  nh.advertise(chatteri);
}

void loop() {
  // put your main code here, to run repeatedly:
  bool button=0;
  if (digitalRead(8)==HIGH){
    button=1;
  }
  bool_msg.data = button;
  V = analogRead(LDRPin);         
  //ilum = ((long)(1024-V)*A*10)/((long)B*Rc*V);  //usar si LDR entre GND y A0 
  ilum = ((long)V*A*10)/((long)B*Rc*(1024-V));    //usar si LDR entre A0 y Vcc (como en el esquema anterior)
  int_msg.data=ilum;
  chatter.publish( &bool_msg );
  chatteri.publish( &int_msg );
  nh.spinOnce();
  delay(500);
}
