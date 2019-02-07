import requests
import json
import os
import datetime

DEFAULT_ENDPOINT = "http://192.168.1.10:5000"

class DataPusher:
    def __init__(self, base_endpoint=DEFAULT_ENDPOINT):
        self.base_endpoint = base_endpoint
        self.post_collection_endpoint = self.base_endpoint + "/collection"

    def push(self, request):
        print("Pushing ", request.files)
        resp = requests.post(self.post_collection_endpoint, files=request.files)
        print (resp.status_code, resp.reason, resp.text)
        if (resp.status_code == requests.codes.ok):
            print ("Pushed to server, deleting..")
            os.remove(request.pic_path)
        else:
            print ("Unable to push data for - leaving in local storage", request.pic_path)

class DataPushRequest:
    def __init__(self, rfid, pic_path, delta_grams):
        self.pic_path = pic_path
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
    