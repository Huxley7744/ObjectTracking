from djitellopy import tello
import KeyPressModule as kp
import time

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 25
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
        yv = -speed
    elif kp.get_key("d"):
        yv = speed
    if kp.get_key("q"):
        me.land()
        time.sleep(1)
    if kp.get_key("e"):
        me.takeoff()
        time.sleep(1)
    return [lr, fb, ud, yv]


while True:
    vals = get_keyboard_input()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.05)
