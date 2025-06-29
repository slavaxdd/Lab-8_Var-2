import cv2


# оригинальная картинка
img = cv2.imread('images/variant-2.png', cv2.IMREAD_COLOR)
cv2.imshow('slon', img)
cv2.waitKey(0)

# нажмите любую клавишу

# блюр по Гауссу (ker size 13)
img_blur = cv2.GaussianBlur(img, (13, 13), 0)

cv2.imwrite('blurred_slon.png', img_blur)
cv2.imshow('blurred slon', img_blur)
cv2.waitKey(0)