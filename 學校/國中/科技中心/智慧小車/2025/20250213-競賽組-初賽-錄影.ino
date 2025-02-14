#include <AFMotor.h>
#include <Servo.h>

Servo servo_9;
Servo servo_10;

AF_DCMotor motor_dc_2(2, MOTOR12_64KHZ);
AF_DCMotor motor_dc_3(3, MOTOR34_64KHZ);

// 描述此函數...
void straight() {
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
  delay(200);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  close_up();
  delay(1000);
  right_turn_0();
  delay(500);
  right_turn_0();
  delay(500);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
  delay(200);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  up();
  delay(100);
  right_turn_0();
  delay(500);
  right_turn_0();
  delay(500);
  stop();
  delay(500);
}

// 描述此函數...
void forward() {
  if ((1023 - analogRead(A0)) >= 500 && (1023 - analogRead(A1)) >= 500) {
    motor_dc_2.setSpeed(200);
    motor_dc_2.run(FORWARD);
    motor_dc_3.setSpeed(200);
    motor_dc_3.run(FORWARD);
  }
  if ((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) >= 500) {
    left_turn_0();
  }
  if ((1023 - analogRead(A0)) >= 500 && (1023 - analogRead(A1)) < 500) {
    right_turn_0();
  }
}

// 描述此函數...
void down_open() {
  servo_10.write(90);
  delay(1000);
  servo_9.write(90);
  delay(1000);
}

// 描述此函數...
void left() {
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  left_turn_1();
  delay(1000);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  close_up();
  delay(1000);
  right_turn_0();
  delay(500);
  right_turn_0();
  delay(600);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  right_turn_1();
  delay(1000);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  delay(100);
  up();
  right_turn_0();
  delay(500);
  right_turn_0();
  delay(500);
  stop();
  delay(500);
}

// 描述此函數...
void right() {
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  right_turn_1();
  delay(1000);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  close_up();
  delay(1000);
  right_turn_0();
  delay(600);
  right_turn_0();
  delay(600);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  left_turn_1();
  delay(1000);
  while (!((1023 - analogRead(A0)) < 500 && (1023 - analogRead(A1)) < 500)) {
    forward();
  }
  stop();
  delay(500);
  down_open();
  up();
  delay(100);
  right_turn_0();
  delay(500);
  right_turn_0();
  delay(500);
  stop();
  delay(500);
}

// 描述此函數...
void backward() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(BACKWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(BACKWARD);
}

// 描述此函數...
void up() {
  servo_10.write(60);
  delay(1000);
}

// 描述此函數...
void stop() {
  motor_dc_2.setSpeed(0);
  motor_dc_2.run(RELEASE);
  motor_dc_3.setSpeed(0);
  motor_dc_3.run(RELEASE);
}

// 描述此函數...
void close_up() {
  servo_9.write(30);
  delay(1000);
  servo_10.write(60);
  delay(1000);
}

// 描述此函數...
void right_turn_0() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(BACKWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
}

// 描述此函數...
void right_turn_1() {
  motor_dc_2.setSpeed(0);
  motor_dc_2.run(RELEASE);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
}

// 描述此函數...
void left_turn_0() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(BACKWARD);
}

// 描述此函數...
void left_turn_1() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(0);
  motor_dc_3.run(RELEASE);
}

// 描述此函數...
void left_turn_2() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(150);
  motor_dc_3.run(FORWARD);
}

// 描述此函數...
void right_turn_2() {
  motor_dc_2.setSpeed(150);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
}


void setup() {

  servo_9.attach(9);
  servo_10.attach(10);
  down_open();

}

void loop() {
  straight();
  left();
  right();

}