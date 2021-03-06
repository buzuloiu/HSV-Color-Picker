import cv2
import numpy as np
import sys

image_hsv = None
pixel = (0, 0, 0)  # RANDOM DEFAULT VALUE

ftypes = [
    ('JPG', '*.jpg;*.JPG;*.JPEG'),
    ('PNG', '*.png;*.PNG'),
    ('GIF', '*.gif;*.GIF'),
]



def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y, x]

        # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        upper = np.array([pixel[0] + 20, pixel[1] + 20, pixel[2] + 40])
        lower = np.array([pixel[0] - 20, pixel[1] - 20, pixel[2] - 40])
        print(lower, upper)

        # A MONOCHROME MASK FOR GETTING A BETTER VISION OVER THE COLORS
        image_mask = cv2.inRange(image_hsv, lower, upper)
        cv2.imshow("Mask", image_mask)


def main(src=None):

    global image_hsv, pixel

    if src:
        image_src = cv2.imread(src)
        cv2.imshow("BGR", image_src)

        # CREATE THE HSV FROM THE BGR IMAGE
        image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", image_hsv)

        # CALLBACK FUNCTION
        cv2.setMouseCallback("HSV", pick_color)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, image_src = video_capture.read()
            cv2.imshow("BGR", image_src)

            # CREATE THE HSV FROM THE BGR IMAGE
            image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV", image_hsv)

            # CALLBACK FUNCTION
            cv2.setMouseCallback("HSV", pick_color)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
