# coding=utf-8
from djitellopy import Tello
from time import sleep  # add some delay between commands

tello = Tello()
tello.connect()
print(tello.get_battery())

# tello.move_forward(25)

tello.takeoff()
tello.send_rc_control(0, 25, 0, 0)  # lr,fb,ud,yaw. [-100, 100]
sleep(2)
tello.send_rc_control(0, 0, 0, 50)  # lr,fb,ud,yaw. [-100, 100]
sleep(2)
tello.send_rc_control(0, 0, 0, 0)  # stop
tello.land()
