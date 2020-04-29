# import open CV Class
import cv2

# import Date and time
from datetime import date

# function readMouse Event
coordinates = [-100, -100]

# facedetection Clasify Trainer it's only working with the gray scale so we need to change the  frame in to gray scale
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# no need for it because x and y is further available in the section
# define event for identify coordiantes to draw rectangle on the video


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.clear()
        coordinates.append(x)
        coordinates.append(y)
        return coordinates

# read Video from file if youwant
# cap = cv2.VideoCapture("Megamind_bugy.avi")


# read video from cam, generally it's on zero if you did not find it you can find it on (-1)
cap = cv2.VideoCapture(0)

# set the video size of your video
cap.set(3, 1024)
cap.set(4, 600)

# http://www.fourcc.org/codecs.php
# Set video encoder
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Set Frame width and height as like video size these functions or codes are available online at open cv portals
framewidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameheight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# save the file as output
out = cv2.VideoWriter("myFile.avi", fourcc,
                      10.0, (framewidth, frameheight))

# Check either the file or cam exisit or not
while (cap.isOpened()):
    # read Frame
    ret, frame = cap.read()

    # http://www.codebind.com/python/opencv-python-tutorial-beginners-read-write-show-videos-camera-opencv/ get the list of codes

    # if frame exisit
    if ret == True:

        # Set Font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # Get Date
        text = date.today()

        # Set Date as text on video top position
        frame = cv2.putText(frame, str(text), (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)

        # Draw coordinates for the rectangle
        frame = cv2.putText(frame, str(coordinates[0]) + ' ,' + str(coordinates[1]), (coordinates[0], coordinates[1]), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)

        # Draw ractangle once you click on the video the square will display
        frame = cv2.rectangle(frame, (coordinates[0], coordinates[1]), (
            coordinates[0]+150, coordinates[1]+150), (0, 255, 255), 1)

        # cv_object_management Properties just for checking
        '''
        print(frame.shape)  # Return The tuple of number row, columns  and channel
        print(frame.size)  # return total number of pixel size
        print(frame.dtype)  # retun data type
        b, r, g = cv2.split(frame)
        print(b)
        print(r)
        print(g)
        '''

        # Start Detecting Face with Haar Cascade Classifiers
        # convert to gray scale because of line number 1 trainer only read the gray scale
        grayScaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayScaleImage, 1.1, 4)

        if len(faces) == 0:
            frame = cv2.putText(frame, "Nice! please keep the mask with you", (150, 150), font, 1,
                                (0, 255, 255), 3, cv2.LINE_AA)

        for(x, y, w, h) in faces:

            cv2.putText(frame, "You did not wear a mask", (x, y), font, 1,
                        (0, 0, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (
                x+w, y+h),  (0, 0, 255), 1)

        # display Video
        cv2.imshow("frame", frame)

        # left click button class mouse event
        cv2.setMouseCallback("frame", click_event)

        # save file if required and frame is there
        out.write(frame)

        # https://https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html get video capture property
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # break the loop on press key q
        if cv2.waitKey(113) == ord('q'):
            break

# relase and distory objects.
cap.release()
out.release()
cv2.destroyAllWindows()
