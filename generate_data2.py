import numpy as np
import cv2
import os
import shutil
import argparse

main_dirC1 = "./data_set_C1"
main_dirC2 = "./data_set_C2"

def main():
    if not os.path.isdir(main_dirC1):
        os.makedirs(main_dirC1)
    else:
        shutil.rmtree(main_dirC1)
        os.makedirs(main_dirC1)
    if not os.path.isdir(main_dirC2):
        os.makedirs(main_dirC2)
    else:
        shutil.rmtree(main_dirC2)
        os.makedirs(main_dirC2)

def generate_img(img_shape):
    img = np.zeros(img_shape, np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img

def generate_shapes(img_shape, n):
    color = [255, 255, 255]
    for j in range(n):
        x_len = np.random.randint(int(img_shape[0])/5, int(img_shape[0])/2)
        y_len = np.random.randint(int(img_shape[0])/5, int(img_shape[0])/2)
        x = np.random.randint(img_shape[0])
        y = np.random.randint(img_shape[0])
        shift = np.random.randint(-(int(img_shape[0])/6+2), int(img_shape[0])/6+2)
        img_1 = cv2.rectangle(generate_img(img_shape), (x, y), (x + x_len, y + y_len), color=color, thickness=-1)
        cv2.imwrite(main_dirC1 + "/" + "[" + str(j) + "]" + str(x_len+1) + "x" + str(y_len+1) + "_A:" + str((x_len+1)*(y_len+1)) + ".png", img_1)
        img_2 = cv2.rectangle(generate_img(img_shape), (x + shift, y), (x + shift + x_len, y + y_len), color=color, thickness=-1)
        cv2.imwrite(main_dirC2 + "/" + "[" + str(j) + "]" + str(x_len+1) + "x" + str(y_len+1) + "_A:" + str((x_len+1)*(y_len+1)) + ".png", img_2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="number of images for training",
                        type=int, required=True)
    parser.add_argument("--img", help="Shape of the generated image", nargs="+", type=int)
    args = parser.parse_args()
    main()
    generate_shapes(tuple(args.img), args.number)
    #cv2.imshow("result", img_)
    #cv2.waitKey(100)