import sys

from scanner import Scanner
from camera import Camera
from data_pusher import *
from weigher import Weigher

scanner = Scanner()
camera = Camera()

weigher = Weigher()

def onTag(rfid):
    pic_path = camera.take_picture(rfid)
    delta_grams = weigher.get_delta()
    dataPusher = DataPusher(rfid, pic_path, delta_grams)
    dataPusher.push()

def main():
    print("Starting waste tracker..")
    while True:
        scanner.poll_sim(onTag)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        base_url = "http://" + sys.argv[1] + ":" + sys.argv[2]
        print("Overwriting default to server endpoint to " + base_url)
        set_base_url(base_url)
    
    main()

