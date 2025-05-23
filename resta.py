import cv2

import numpy as np

fn = np.zeros((413, 930, 3), np.uint8)
cv2.circle(fn, (617, 245), (777-617), (255, 255, 255), -1)
img = cv2.imread("tenis.jpg")

while True:
    img2 = cv2.subtract(fn, img)
    # cv2.add
    cv2.imshow("d", img2)

    if cv2.waitKey(1) == ord('h'):
        break
cv2.destroyAllWindows()
