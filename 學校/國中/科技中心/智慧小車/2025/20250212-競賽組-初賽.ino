#include <Servo.h>
#include <AFMotor.h>

int limit_between_black_and_white;
int time_of_move_center_of_car_to_center_of_intersect;
int time_of_across_black_line;
int time_of_turn_90deg;
Servo servo_9;
Servo servo_10;

AF_DCMotor motor_dc_2(2, MOTOR12_64KHZ);
AF_DCMotor motor_dc_3(3, MOTOR34_64KHZ);

// 描述此函數...
void pick_left() {
  follow();
  L_left_turn();
  follow();
  pick();
  U_turn();
  follow();
  L_right_turn();
  follow();
  down_and_open();
  U_turn();
}

// 描述此函數...
void pick_middle() {
  follow();
  forward_across();
  follow();
  pick();
  U_turn();
  follow();
  forward_across();
  follow();
  down_and_open();
  U_turn();
}

// 描述此函數...
void pick_right() {
  follow();
  L_right_turn();
  follow();
  pick();
  U_turn();
  follow();
  L_left_turn();
  follow();
  down_and_open();
  U_turn();
}

// 描述此函數...
void up() {
  servo_10.write(60);
  delay(1000);
}

// 描述此函數...
void down() {
  servo_10.write(90);
  delay(1000);
}

// 描述此函數...
void open() {
  servo_9.write(90);
  delay(1000);
}

// 描述此函數...
void close() {
  servo_9.write(30);
  delay(1000);
}

// 描述此函數...
void down_and_open() {
  down();
  open();
}

// 描述此函數...
void close_and_up() {
  close();
  up();
}

// 描述此函數...
void follow() {
  while (!((1023 - analogRead(A0)) < limit_between_black_and_white && (1023 - analogRead(A1)) < limit_between_black_and_white)) {
    if ((1023 - analogRead(A0)) >= limit_between_black_and_white && (1023 - analogRead(A1)) >= limit_between_black_and_white) {
      forward();
    } else if ((1023 - analogRead(A0)) < limit_between_black_and_white && (1023 - analogRead(A1)) >= limit_between_black_and_white) {
      turn_left_inplace();
    } else if ((1023 - analogRead(A0)) >= limit_between_black_and_white && (1023 - analogRead(A1)) < limit_between_black_and_white) {
      turn_right_inplace();
    } else if ((1023 - analogRead(A0)) < limit_between_black_and_white && (1023 - analogRead(A1)) < limit_between_black_and_white) {
      stop();
      break;
    }
  }
}

// 描述此函數...
void forward_across() {
  forward();
  delay(time_of_across_black_line);
  stop();
}

// 描述此函數...
void forward() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
}

// 描述此函數...
void backward() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(BACKWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(BACKWARD);
}

// 描述此函數...
void stop() {
  motor_dc_2.setSpeed(0);
  motor_dc_2.run(RELEASE);
  motor_dc_3.setSpeed(0);
  motor_dc_3.run(RELEASE);
}

// 描述此函數...
void turn_left_inplace() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(FORWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(BACKWARD);
}

// 描述此函數...
void turn_right_inplace() {
  motor_dc_2.setSpeed(200);
  motor_dc_2.run(BACKWARD);
  motor_dc_3.setSpeed(200);
  motor_dc_3.run(FORWARD);
}

// 描述此函數...
void L_left_turn() {
  forward();
  delay(time_of_move_center_of_car_to_center_of_intersect);
  turn_left_inplace();
  delay(time_of_turn_90deg);
  stop();
}

// 描述此函數...
void L_right_turn() {
  forward();
  delay(time_of_move_center_of_car_to_center_of_intersect);
  turn_right_inplace();
  delay(time_of_turn_90deg);
  stop();
}

// 描述此函數...
void U_turn() {
  forward();
  delay(time_of_move_center_of_car_to_center_of_intersect);
  turn_left_inplace();
  delay((time_of_turn_90deg * 2));
  stop();
}

// 描述此函數...
void pick() {
  down_and_open();
  delay(100);
  close_and_up();
}


void setup() {

  limit_between_black_and_white = 500;
  time_of_move_center_of_car_to_center_of_intersect = 350;
  time_of_across_black_line = 150;
  time_of_turn_90deg = 600;
  servo_9.attach(9);
  servo_10.attach(10);

}

void loop() {
  pick_left();
  pick_middle();
  pick_right();

}