import time
import pygame
import KeyPressModule as kp
from djitellopy import Tello
import cv2


def get_keyboard_input():
    lr, fb, ud, yaw = 0, 0, 0, 0
    speed = 25
    if kp.get_key("e"):
        tello.takeoff()

    if kp.get_key("q"):
        tello.land()

    if kp.get_key("LEFT"):
        lr = -speed
    elif kp.get_key("RIGHT"):
        lr = speed

    if kp.get_key("UP"):
        fb = speed
    elif kp.get_key("DOWN"):
        fb = -speed

    if kp.get_key("w"):
        ud = speed
    elif kp.get_key("s"):
        ud = -speed

    if kp.get_key("a"):
        yaw = -speed
    elif kp.get_key("d"):
        yaw = speed

    if kp.get_key("z"):
        cv2.imwrite(f'resources/images/{time.time()}.jpg', frame)
        time.sleep(0.3)

    return [lr, fb, ud, yaw]


if __name__ == "__main__":
    kp.init()
    tello = Tello()
    tello.connect()
    print(tello.get_battery())
    tello.streamon()

    global frame

    while True:

        vals = get_keyboard_input()
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

        frame = tello.get_frame_read().frame
        frame = cv2.resize(frame, (300, 200))
        cv2.imshow("tello_frame", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    tello.streamoff()
    cv2.destroyAllWindows()
