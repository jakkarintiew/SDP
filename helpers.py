from matplotlib import pyplot as plt
from matplotlib.colors import hsv_to_rgb
import cv2

# Some helper functions
def show1img(img_title, img):
#     img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    figure_size = 10
    plt.figure(figsize=(figure_size, figure_size))
    plt.imshow(img)
    plt.title(img_title)
    plt.show()

def show2img(img1_title, img1,img2_title, img2):
#     img1 =  cv2.cvtColor(img1, cv2.COLOR_HSV2RGB)
#     img2 =  cv2.cvtColor(img2, cv2.COLOR_HSV2RGB)
    figure_size = 20
    plt.figure(figsize=(figure_size, figure_size))
    plt.subplot(1, 2, 1), plt.imshow(img1)
    plt.title(img1_title), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(img2)
    plt.title(img2_title), plt.xticks([]), plt.yticks([])

    plt.show()

