import time

from goprocam import GoProCamera, constants

gpCam = GoProCamera.GoPro()
print(gpCam.take_photo(10))
