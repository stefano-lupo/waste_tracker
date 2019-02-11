import os

# from picamera import PiCamera

dir_path = os.path.dirname(os.path.realpath(__file__))
tmp_image_path = dir_path + "/tmp_images"

class Camera:
    # camera = PiCamera()
    # camera.resolution = (1920, 1080)

    def __init__(self):
        print("Created camera instance")
    
    def take_picture(self, id):
        print("Taking picture for: ", id)
        outpath = tmp_image_path + "/" + str(id) + ".jpg"
        # self.camera.capture(outpath)
        outpath = "ignoreme"
        return outpath
    