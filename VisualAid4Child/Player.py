from imutils.video import FPS
from ffpyplayer.player import MediaPlayer
import imutils
import numpy
import cv2 as cv
import time
import os

def playerHelper(class_name):
    path = 'videos/'+ class_name +'.MP4'
    if not os.path.isfile(path):
        print('Playing file is not found...')
    else:
        vidcap = cv.VideoCapture(path)
        player = MediaPlayer(path)
        #fps = FPS().start()
        #val = ''
        #print ('Detected' + class_name)
        while(vidcap.isOpened()):
            vidret, frame = vidcap.read()
            #ffpframe, ffpval = player.get_frame()

            if not vidret:# and val != 'eof' and ffpframe is not None:
                #ffpframe, ffpt = ffpframe
                break

            time.sleep(0.0248)
            frame = imutils.resize(frame, width=450)
            #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            #frame = numpy.dstack([frame, frame, frame])

            cv.imshow('Playing for, ' + class_name, frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            # fps.update()

        # fps.stop()
        vidcap.release()
        # player.release()
        cv.destroyAllWindows()