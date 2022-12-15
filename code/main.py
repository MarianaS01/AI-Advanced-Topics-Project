from predict_functions import *
import cv2 as cv

DIST_Z = 63 # cm
WIDTH_CM = 56 # cm
HEIGHT_CM = 65 # cm

X0 = 1330 # px
X1 = 1750 # px
Y0 = 1040 # px
Y1 = 1760 # px

center = ((X1 - X0)//2, (Y1 - Y0)//2)

def pixels_to_cartesian(point:tuple):
    """
    * pixel_dims: (width, height) 
    """
    x_pxl, y_pxl = point
    cart_x = round(x_pxl * WIDTH_CM  / DIMS_PXLS[0], 2) 
    cart_y = round(y_pxl * HEIGHT_CM / DIMS_PXLS[1], 2) 
    return cart_x, cart_y

# 1. Image Read
img_path = 'images/manzanita.jpg'
img = cv.imread(img_path)
height_pxls = img.shape[0]
width_pxls = img.shape[1]
DIMS_PXLS = (width_pxls, height_pxls)
print(DIMS_PXLS)
# 2. Crop Image
cropped_img = img[Y0: Y1, X0: X1]
cv.imwrite('images/cropped_img.jpg', cropped_img)

# 3. Classify Image
class_name, prob = predict('images/cropped_img.jpg')

# 4. Image Location
# if the center of the rectangle is specified, the robot
# should move to that point and there close the gripper
cart_x, cart_y = pixels_to_cartesian(center)
bx, by = pixels_to_cartesian((X0, Y0))
cart_x += bx
cart_y += by

print('------------------------------')
print('The image is a: ', class_name)
print('With a certainty of: {0:.2f}%'.format(prob))
print('------------------------------')
print('This object is located at: x: {}cm, y: {}cm, z: {}cm'.format(cart_x, cart_y, DIST_Z))

img_rect = cv.rectangle(img, (X0, Y0), (X1, Y1), color=(0, 255, 0), thickness=25)
output = cv.resize(img_rect, (400, 600))
cv.imshow('Image', output)
cv.waitKey(0)