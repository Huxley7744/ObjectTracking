# coding=utf-8
from djitellopy import Tello
from time import sleep  # add some delay between command
import cv2

tello = Tello()
tello.connect()
print(tello.get_battery())

tello.streamon()

while True:
    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (300, 200))
    cv2.imshow("tello_frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    # cv2.waitKey(1)
tello.streamoff()
cv2.destroyAllWindows()
