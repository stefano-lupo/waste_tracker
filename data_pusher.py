import requests
import json
import os
import datetime

BASE_ENDPOINT= "http://192.168.1.10:5000"
IMG_ENDPOINT = BASE_ENDPOINT + "/collection"

class DataPusher:
    def __init__(self, rfid, pic_path, delta_grams):
        print("Data pusher constructor")
        self.pic_path = pic_path
        self.build_request(rfid, delta_grams)
                
    def build_request(self, rfid, delta_grams):
        timestamp = datetime.datetime.now().isoformat()
        rfid_str = str(rfid)
        payload = {
            "rfid": rfid_str,
            "weight": delta_grams,
            "collected_timestamp": timestamp
        }
        image = open(self.pic_path, 'rb')
        self.files = {
            'json': (None, json.dumps(payload), 'application/json'),
            'image': (rfid_str + "_" + timestamp + ".jpg", image, 'application/octet-stream')
        }
    
    def push(self):
        print("Pushing ", self.files)
        resp = requests.post(IMG_ENDPOINT, files=self.files)
        print (resp.status_code, resp.reason, resp.text)
        if (resp.status_code == requests.codes.ok):
            print ("Pushed to server, deleting..")
            os.remove(self.pic_path)
        else:
            print ("Unable to push data for - leaving in local storage", self.pic_path)

def set_base_url(base_endpoint):
    BASE_ENDPOINT = base_endpoint