# from pirc522 import *
# from pirc522 import RFID
from pirc522 import RFID
import uuid

class Scanner:
    # rdr = RFID() # This also only works on a pi

    def __init__(self):
        print("Scanner started")
    
    def poll_sim(self, callback):
        print("Press any key to simulate RFID read")
        input()
        id = uuid.uuid4()
        print("Simulating RFID ID = ", id)
        callback(id)
    
    # def pollRFIDReader():
#     while True:
#     rdr.wait_for_tag()
#     (error, tag_type) = rdr.request()
#     if not error:
#         print("Tag detected")
#         (error, uid) = rdr.anticoll()
#         if not error:
#         print("UID: " + str(uid))
#         # Select Tag is required before Auth
#         if not rdr.select_tag(uid):
#             # Auth for block 10 (block 2 of sector 2) using default shipping key A
#             if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
#             # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#             print("Reading block 10: " + str(rdr.read(10)))
#             # Always stop crypto1 when done working
#             rdr.stop_crypto()
    # Calls GPIO cleanup
    # rdr.cleanup()