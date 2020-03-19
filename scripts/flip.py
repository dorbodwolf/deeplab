# encoding:utf-8
import cv2
import sys
import os

def main():
    in_img = sys.argv[1]
    out_path = sys.argv[2]
    image = cv2.imread(in_img)

    # Flipped Horizontally 水平翻转
    h_flip = cv2.flip(image, 1)
    cv2.imwrite(out_path+os.path.basename(in_img)[:-4]+'_flip.tif', h_flip)


if __name__ == "__main__":
    main()