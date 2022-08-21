import cv2
import math
goalx = 530
goaly = 300
video = cv2.VideoCapture("PRO-C107-Reference-Code-main/bb3.mp4")
tracker = cv2.TrackerCSRT_create()
ret, img = video.read()
bBox = cv2.selectROI("tracking", img, False)
tracker.init(img, bBox)
xs=[]
ys=[]


def drawBox(image, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


def goalTracking(image, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(image, (c1, c2), 2, (0, 0, 255), 3)
    cv2.circle(image, (goalx, goaly), 2, (0, 0, 255), 3)
    dist = math.sqrt(((c1-goalx)**2) + (c2-goaly)**2)
    xs.append(c1);
    ys.append(c2);
    if (dist < 40):
        cv2.putText(image, "Goal", (350, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    for i in range(len(xs)-1):
        cv2.circle(image, (xs[i], ys[i]), 2, (0, 0, 255), 3)



while True:
    ret, image = video.read()
    success, bBox = tracker.update(image)
    if (success == True):
        drawBox(image, bBox)
    goalTracking(image, bBox)
    cv2.imshow("reasult", image)
    if cv2.waitKey(1) == 32:
        break
video.release()
cv2.destroyAllWindows()
