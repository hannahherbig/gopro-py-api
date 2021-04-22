from goprocam import GoProCamera, constants

gpCam = GoProCamera.GoPro()
TIMER=4
gpCam.downloadLastMedia(gpCam.take_photo(TIMER)) #take a photo in 4 seconds and download it.
