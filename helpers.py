from matplotlib import pyplot as plt

# Some helper functions
def show1img(img, img_title):
    figure_size = 10
    plt.figure(figsize=(figure_size, figure_size))
    plt.imshow(img)
    plt.title(img_title)

    plt.show()


def show2img(img1, img1_title, img2, img2_title):
    figure_size = 20
    plt.figure(figsize=(figure_size, figure_size))
    plt.subplot(1, 2, 1), plt.imshow(img1)
    plt.title(img1_title), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(img2)
    plt.title(img2_title), plt.xticks([]), plt.yticks([])

    plt.show()

