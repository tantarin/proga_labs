import cv2
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--image')

args = parser.parse_args() # python main.py --image pic.jpg


facePhoto = "highlight/opencv_face_detector.pbtxt"
faceModel = "highlight/opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, facePhoto)

genderProto="detection/gender_deploy.prototxt"
genderModel="detection/gender_net.caffemodel"
ageProto="detection/age_deploy.prototxt"
ageModel="detection/age_net.caffemodel"

# настраиваем свет
MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)

# итоговые результаты работы нейросетей для пола и возраста
genderList=['Male ','Female']
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# запускаем нейросети по определению пола и возраста
genderNet=cv2.dnn.readNet(genderModel,genderProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)


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


def face_finder():
    video = cv2.VideoCapture(args.image if args.image else 0)

    while cv2.waitKey(1) < 0:
        hasFrame, frame = video.read()

        if not hasFrame:
            cv2.waitKey()
            break

        resultImg, faceBoxes = highlightFace(faceNet, frame)

        for faceBox in faceBoxes:
            # получаем изображение лица на основе рамки
            face=frame[max(0,faceBox[1]):
                    min(faceBox[3],frame.shape[0]-1),max(0,faceBox[0])
                    :min(faceBox[2], frame.shape[1]-1)]
            # получаем на этой основе новый бинарный пиксельный объект
            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            # отправляем его в нейросеть для определения пола
            genderNet.setInput(blob)
            # получаем результат работы нейросети
            genderPreds=genderNet.forward()
            # выбираем пол на основе этого результата
            gender=genderList[genderPreds[0].argmax()]
            # отправляем результат в переменную с полом
            print(f'Gender: {gender}')

            # делаем то же самое для возраста
            ageNet.setInput(blob)
            agePreds=ageNet.forward()
            age=ageList[agePreds[0].argmax()]
            print(f'Age: {age[1:-1]} years')

            # добавляем текст возле каждой рамки в кадре
            cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
            # выводим итоговую картинку
            cv2.imshow("Detecting age and gender", resultImg)

        if not faceBoxes:
            print('Лица не распознаны')


if __name__ == "__main__":
    face_finder()
