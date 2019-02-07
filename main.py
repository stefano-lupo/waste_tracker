from Scanner import *
from Camera import Camera
from DataPusher import *

scanner = Scanner()
camera = Camera()
dataPusher = DataPusher()

def onTag(id):
    pic_path = camera.take_picture(id)
    dataPusher.push(id, pic_path)

def main():
    print("Starting waste tracker..")
    while True:
        scanner.poll_sim(onTag)

if __name__ == '__main__':
    main()

