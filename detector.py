import cv2

plateNumberCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

def detect(image):
    imageCopy = image.copy()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    try:
        plateNumbers = plateNumberCascade.detectMultiScale(imageGray, 1.1, 10)
        for (x, y, w, h) in plateNumbers:
            area = w*h
            if area > 200:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 255), 2)
                cv2.putText(image, "Plate Number", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                roi = image[y:y+h, x:x+w]
                cv2.imshow("ROI", roi)
        cv2.imshow("Original", imageCopy)
        cv2.imshow("Output", image)
    except:
        print("No Plate Numbers detected")


def show_video(cap):
    while True:
        _, image = cap.read()
        detect(image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def detector():
    path = input("Enter path to an image or video: ")
    if path.endswith(('.jpg', '.jpeg', '.png', '.svg')):
        image = cv2.imread(path)
        detect(image)
        cv2.waitKey()
    elif path.endswith(('.mp4', '.mov', '.gif', '.webm')):
        cap = cv2.VideoCapture(path)
        show_video(cap)
    elif path == '0':
        cap = cv2.VideoCapture(0)
        show_video(cap)
    else:
        print("Invalid input")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detector()