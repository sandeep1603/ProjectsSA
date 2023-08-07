import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

DIM = (1280, 800) 
K = np.array([[507.68698532761493, 0.0, 655.3366354484476], [0.0, 512.1594339642056, 452.7337574172289], [0.0, 0.0, 1.0]])  
D = np.array([[-0.1631706015004709], [0.3656816985307999], [-0.7317339516726239], [0.4573029988045851]])  

def undistort(img_path):
    print("Processing:", img_path)
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Unable to read the image from", img_path)
        return

    h, w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    undistorted_img = cv2.resize(undistorted_img, (w, h))

    combined_img = np.hstack((img, undistorted_img))

    img_name, img_ext = os.path.splitext(os.path.basename(img_path))
    save_path = os.path.join(os.path.dirname("C:/Users/sagayaraj/Desktop/PythonTest/Sandeep/Fisheye/Image/undistorted image"), img_name + "_undistorted" + img_ext)
    cv2.imwrite(save_path, undistorted_img)


    plt.imshow(cv2.cvtColor(combined_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    image_dir = "C:/Users/sagayaraj/Desktop/PythonTest/Sandeep/Fisheye/Image"  
    image_files = glob.glob(os.path.join(image_dir, "*.jpg"))
    for img_path in image_files:
        undistort(img_path)