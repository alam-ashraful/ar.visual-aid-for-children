from imutils.video import FPS
import imutils
import cv2 as cv
import numpy
import time
import Player as P

classNames = { 1: 'person',
               44: 'bottle',
               47: 'cup',
               49: 'knife',
               50: 'spoon',
               52: 'banana',
               73: 'laptop',
               77: 'cell phone',
               84: 'book'
               }

cvNet = cv.dnn.readNetFromTensorflow('model/frozen_inference_graph.pb',
                                     'model/ssd_mobilenet_v1_coco_2017_11_17.pbtxt')

IGNORE = set({'person'})
cap = cv.VideoCapture(0)
while True:

    ret, img = cap.read()

    cvNet.setInput(cv.dnn.blobFromImage(img, 0.007843, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    detections = cvNet.forward()
    # cols = img.shape[1]
    # rows = img.shape[0]
    (h, w, d) = img.shape
    cols = w
    rows = h

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.4:
            class_id = int(detections[0, 0, i, 1])
            #if classNames[class_id] in IGNORE:
                    #continue
            if class_id in classNames:
                
                print('Class id: {0}\nClass name: {1}\nScores: {2:.2f}'
                      .format
                      (class_id,
                       classNames[class_id],
                       100*confidence)
                      )

                if classNames[class_id] not in IGNORE:
                    P.playerHelper(classNames[class_id])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop = int(detections[0, 0, i, 5] * cols)
                yRightTop = int(detections[0, 0, i, 6] * rows)

                cv.rectangle(img, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                             (0, 255, 0))
                if class_id in classNames:
                    label = 'Detected as, {0} Scores: {1:.2f}%'.format(classNames[class_id],confidence*100)
                    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                    yLeftBottom = max(yLeftBottom, labelSize[1])
                    cv.putText(img, label, (xLeftBottom + 50, yLeftBottom + 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
                    #input("Press Enter to continue...")

            cv.imshow('Object recognization', img)
            # if cv.waitKey(1) & 0xFF == ord('q'):
            #     break
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
