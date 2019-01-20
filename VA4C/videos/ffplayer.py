from ffpyplayer.player import MediaPlayer
import time
import cv2 as cv

vid = 'bottle.MP4'
player = MediaPlayer(vid)
val = ''
while val != 'eof':
    ffpframe, ffpval = player.get_frame()
    if val != 'eof' and ffpframe is not None:
        ffpframe, ffpt = ffpframe

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
player.release()
cv.destroyAllWindows()
    
