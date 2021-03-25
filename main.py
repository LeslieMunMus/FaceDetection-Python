import cv2
import glob

"""

THE COMMENTED OUT CODE IS FACE DETECTION FOR SINGLE SPECIFIC FILES IN THE SAME DIRECTORY:

# Cascade classifier using our haar cascade xml file
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Capture frames from a video or image. Use cv2.VideoCapture(0) for video cam or file name for image file
imp_img = cv2.VideoCapture("elon1.jpg")

# Read image. True if it reads the image or false if it doesn't. Also returns pixel dimension
res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale for haar to work

# Detect faces of different sizes in the input image
faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:  # Draw square around recognised face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

# Show image
cv2.imshow("Elon Image", img)

# THESE 3 STEPS SHOULD BE DONE ALWAYS
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()


"""

all_images = glob.glob("*.jpg")
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_images:
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        final_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow("Face Detection", final_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


"""

There are many haar cascade files for different detections eg. eyes, smile, vehicles etc.
You just have to download the correct haar cascade file that corresponds with what you want to do

"""