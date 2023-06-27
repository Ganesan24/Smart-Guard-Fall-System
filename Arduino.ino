void setup(){
     pinMode(12,OUTPUT); // RELAY PIN   

  Serial.begin(9600);
}

void loop(){
      digitalWrite(12,HIGH); 
  delay(3000);

  
  int human_count;

  if (Serial.available() > 0) {
    human_count = Serial.parseInt();
  }

     if(human_count >= 0){
      digitalWrite(12,LOW);
      delay(2000);
      digitalWrite(12,HIGH);
        
      }
  
  
  
  
  
  }