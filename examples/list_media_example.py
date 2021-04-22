import time

from goprocam import GoProCamera, constants

gpCam = GoProCamera.GoPro(constants.auth)
gpCam.overview()
gpCam.listMedia(True)
