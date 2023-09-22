import os
import cv2
import tkinter as tk
from tkinter import filedialog


def loadFaceRecognitionModel():
    facePhoto = "opencv_face_detector.pbtxt"
    faceModel = "opencv_face_detector_uint8.pb"
    return cv2.dnn.readNet(faceModel, facePhoto)


def processImage(faceNet, image_path):
    if not os.path.exists(image_path) or not os.path.isfile(image_path):
        print(f"Файл '{image_path}' не существует или не доступен для чтения.")
        return

    frame = cv2.imread(image_path)
    resultImg, faceBoxes = highlightFace(faceNet, frame)

    if not faceBoxes:
        print('Лица не распознаны')
    cv2.imshow("Распознавание лиц", resultImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        faceNet = loadFaceRecognitionModel()
        processImage(faceNet, file_path)


def main():
    root = tk.Tk()
    root.title("Распознавание лиц")

    browse_button = tk.Button(root, text="Выбрать изображение", command=browse_image)
    browse_button.pack()

    exit_button = tk.Button(root, text="Выход", command=root.destroy)
    exit_button.pack()

    root.mainloop()


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()

    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]

    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)

            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 225, 0), int(round(frameHeight / 150)), 8)

    return frameOpencvDnn, faceBoxes


if __name__ == "__main__":
    main()
