import sys
from signal import SIGINT, signal

from goprocam import GoProCamera, constants

gopro = GoProCamera.GoPro(ip_address=GoProCamera.GoPro.getWebcamIP(
    sys.argv[1]), camera=constants.gpcontrol, webcam_device=sys.argv[1])


def handler(s, f):
    gopro.stopWebcam()
    quit()


signal(SIGINT, handler)

# gopro.startWebcam(constants.Webcam.Resolution.R720p)
gopro.webcamFOV(constants.Webcam.FOV.Linear)
gopro.getWebcamPreview()
gopro.KeepAlive()
