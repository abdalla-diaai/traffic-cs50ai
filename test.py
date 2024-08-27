from traffic import *
import os
import cv2 as cv

DIR_PATH = "gtsrb-small"
# list to store files name
images = []
labels = []
for dir in os.listdir(DIR_PATH):
    # build the path to the folder
    folder_path = os.path.join(DIR_PATH, dir)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            img = cv.imread(file_path)
            res = cv.resize(img,(IMG_WIDTH, IMG_HEIGHT))
            labels.append(dir)
            images.append(res)

print(len(labels))
np.array(images)
