import subprocess

initialized = False

class Camera:
    def takePhoto(self, filepath):
        subprocess.call('fswebcam -r 1280x960 -q --jpeg 95 --save {}'.format(filepath), shell=True)

