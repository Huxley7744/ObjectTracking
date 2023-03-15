import time
import cv2
from djitellopy import Tello

# parameters
w, h = 360, 240
counter = 0  # 1 for test, 0 for flight

# connect to Tello
tello = Tello()
tello.connect()
tello.for_back_velocity = 0
tello.left_right_velocity = 0
tello.up_down_velocity = 0
tello.yaw_velocity = 0
tello.speed = 0

time.sleep(3)

tello.streamon()

print ("battery: ", tello.get_battery())

while True:
    # get out frame
    frame_read = tello.get_frame_read()
    myFrame = frame_read.frame
    frame = cv2.resize(myFrame, (w, h))

    # if this is the first frame, takeoff
    if counter == 0:
        time.sleep(3)
        tello.takeoff()
        time.sleep(3)
        tello.rotate_clockwise(180)
        time.sleep(3)
        tello.land()
        counter = 1

    cv2.imshow("Tello", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
