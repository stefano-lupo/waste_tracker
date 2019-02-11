import sys
import time

from scanner import Scanner
from camera import Camera
from data_pusher import DataPusher, DataPushRequest
from weigher import Weigher

SLEEP_TIME_SEC = 3

data_pusher = DataPusher()
scanner = Scanner()
camera = Camera()
weigher = Weigher()

def onTag(rfid):
    # pic_path = camera.take_picture(rfid)
    pic_path = "tmp_images/spinthing.png"
    delta_grams = weigher.get_delta()
    print("Weight: %d" % delta_grams)
    data_push_request = DataPushRequest(rfid, pic_path, delta_grams)
    data_pusher.push(data_push_request)

def main():
    print("Starting waste tracker..")
    while True:
        scanner.poll_sim(onTag)
        time.sleep(SLEEP_TIME_SEC)

def cleanup():
    weigher.cleanup()
    scanner.cleanup()

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        base_url = "http://" + sys.argv[1] + ":" + sys.argv[2]
        print("Overwriting default to server endpoint to " + base_url)
        data_pusher = DataPusher(base_url)    
    main()

