import requests

base_endpoint= "http://192.168.1.10:5000"
img_endpoint = base_endpoint + "/image"

class DataPusher:

    def __init__(self):
        print("Data pusher constructor")

    def push(self, id, pic_path):
        print("Pushing - ", id, pic_path)
        with open(pic_path, 'rb') as f:

            r = requests.post(img_endpoint, files={'image': f})
            print (r.status_code, r.reason)
    