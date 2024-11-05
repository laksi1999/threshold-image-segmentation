import cv2
import numpy as np


def convert_to_gray_scale(image):
    R, G, B = 0.21, 0.72, 0.07

    r_channel = image[:, :, 0]
    g_channel = image[:, :, 1]
    b_channel = image[:, :, 2]

    gray_scale_image = R * r_channel + G * g_channel + B * b_channel

    gray_scale_image = gray_scale_image.astype("uint8")

    return gray_scale_image


image = cv2.imread("c_image.webp")

gray_scale_image = convert_to_gray_scale(image)

T0 = np.mean(gray_scale_image)

while True:
    M1 = gray_scale_image[np.where(gray_scale_image >= T0)].mean()
    M2 = gray_scale_image[np.where(gray_scale_image < T0)].mean()

    T = (M1 + M2) / 2

    if T == T0: break

    T0 = T

gray_scale_image[np.where(gray_scale_image >= T)] = np.uint8(255)
gray_scale_image[np.where(gray_scale_image < T)] = np.uint8(0)

cv2.imwrite(f"c_segmented_image.jpg", gray_scale_image)
