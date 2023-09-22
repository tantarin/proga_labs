import os

import cv2


def loadFaceRecognitionModel():
    facePhoto = "opencv_face_detector.pbtxt"
    faceModel = "opencv_face_detector_uint8.pb"
    return cv2.dnn.readNet(faceModel, facePhoto)


def processVideoOrImage(faceNet, option):
    if option == "1":
        video = cv2.VideoCapture(0)
    elif option == "2":
        image_name = input("Введите имя изображения (например, 'name.jpg'):\n")
        image_path = "pictures/" + image_name
        if not os.path.exists(image_path) or not os.path.isfile(image_path):
            print(f"Файл '{image_path}' не существует или не доступен для чтения.")
            return
        video = cv2.VideoCapture(image_path)
    else:
        print("Выбрана неверная опция")
        return

    while cv2.waitKey(1) < 0:
        hasFrame, frame = video.read()
        if not hasFrame:
            cv2.waitKey()
            break

        resultImg, faceBoxes = highlightFace(faceNet, frame)

        if not faceBoxes:
            print('Лица не распознаны')

        cv2.imshow("Распознавание лиц", resultImg)


def main():
    faceNet = loadFaceRecognitionModel()

    while True:
        option = input("'1': Видео\n'2': Изображение\n'q': Выход\n")
        if option == "q":
            break
        processVideoOrImage(faceNet, option)


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


if __name__ == "__main__":
    main()
