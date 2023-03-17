import time
import cv2
from djitellopy import Tello

# parameters
w, h = 360, 240
counter = 1  # 1 for test, 0 for flight

# connect to Tello
tello = Tello()
tello.connect()
tello.send_rc_control(0, 0, 0, 0)

tello.streamon()
time.sleep(3)

print("battery: ", tello.get_battery())

while True:
    # get out frame
    frame_read = tello.get_frame_read()
    myFrame = frame_read.frame
    frame = cv2.resize(myFrame, (w, h))

    # show the frame
    cv2.imshow("Tello", frame)

    # if this is the first frame, takeoff
    if counter == 0:
        tello.takeoff()
        tello.send_rc_control(0, 0, 0, 50)
        time.sleep(2.5)
        tello.send_rc_control(0, 0, 0, 0)
        tello.land()
        counter = 1

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

tello.streamoff()
cv2.destroyAllWindows()
