import cv2

facePhoto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, facePhoto)

def main():
    while True:
        ans = (input("'1' - Video Finder\n'2' - Picture Finder\n"))
        if ans == "1":
            video_finder()
            break
        else:
            image = (input("Which image? (for example: '1.jpg')\n"))
            cv2.imshow('New Image', picture_finder(faceNet, image))
            cv2.waitKey(0)
            break


def picture_finder(net, image, conf_threshold=0.7):
    imageOpencvDnn = cv2.imread("faces/" + image)

    imageHeight = imageOpencvDnn.shape[0]
    imageWidth = imageOpencvDnn.shape[1]

    blob = cv2.dnn.blobFromImage(imageOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob) 

    detections = net.forward()

    faceBoxes = []

    for _i in range(detections.shape[2]):
        confidence = detections[0, 0, _i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, _i, 3] * imageWidth)
            y1 = int(detections[0, 0, _i, 4] * imageHeight)

            x2 = int(detections[0, 0, _i, 5] * imageWidth)
            y2 = int(detections[0, 0, _i, 6] * imageHeight)

            faceBoxes.append([x1, y1, x2, y2])

            cv2.rectangle(imageOpencvDnn, (x1, y1), (x2, y2), (0, 225, 0), int(round(imageHeight/150)), 8)

    cv2.imwrite("faces/" + image[:-4] + "_face_found.jpg", imageOpencvDnn)
    return imageOpencvDnn


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()

    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]

    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)

    detections = net.forward()

    faceBoxes = []

    for _i in range(detections.shape[2]):
        confidence = detections[0, 0, _i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, _i, 3] * frameWidth)
            y1 = int(detections[0, 0, _i, 4] * frameHeight)

            x2 = int(detections[0, 0, _i, 5] * frameWidth)
            y2 = int(detections[0, 0, _i, 6] * frameHeight)

            faceBoxes.append([x1, y1, x2, y2])

            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 225, 0), int(round(frameHeight/150)), 8)

        return frameOpencvDnn, faceBoxes 


def video_finder():
    video = cv2.VideoCapture(0)

    while cv2.waitKey(1) < 0:
        hasFrame, frame = video.read()

        if not hasFrame:
            cv2.waitKey()
            break

        resultImg, faceBoxes = highlightFace(faceNet, frame)

        if not faceBoxes:
            print('Лица не распознаны')


        cv2.imshow("Face recognition", resultImg)


if __name__ == "__main__":
    main()
