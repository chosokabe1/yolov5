import os
import cv2
import sys

args = sys.argv
img_path = args[1]
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
txt_path = "runs/detect/egg_or_not/labels/" + os.path.splitext(os.path.basename(img_path))[0] + ".txt"
if not os.path.exists(txt_path):
    sys.exit()

save_dir = "runs/detect/egg_or_not/microbial_region"
makedir(save_dir)
save_tmp_train_a = "runs/detect/egg_or_not/tmp/train/a"
makedir(save_tmp_train_a)
save_tmp_train_b = "runs/detect/egg_or_not/tmp/train/b"
makedir(save_tmp_train_b)
save_tmp_val_a = "runs/detect/egg_or_not/tmp/val/a"
makedir(save_tmp_val_a)
save_tmp_val_b = "runs/detect/egg_or_not/tmp/val/b"
makedir(save_tmp_val_b)

img = cv2.imread(img_path)
print(img.shape)
txt_path = "runs/detect/egg_or_not/labels/" + os.path.splitext(os.path.basename(img_path))[0] + ".txt"
with open(txt_path) as f:
    s = f.readlines()
    print(s)
    count = 0
    for line in s:
        split = line.split()
        if split:
            center_x_float = float(split[1])
            center_y_float = float(split[2])
            width_float    = float(split[3])
            height_float   = float(split[4])
    
            print(center_x_float)  
            print(center_y_float)
            print(width_float)  
            print(height_float)
            print(img.shape)
            center_x_int = round(img.shape[1] * center_x_float)
            center_y_int = round(img.shape[0] * center_y_float)
            width_int    = round(img.shape[1] * width_float)
            height_int   = round(img.shape[0] * height_float)
            kiri_left = center_x_int - width_int // 2
            kiri_right = kiri_left + width_int
            kiri_top = center_y_int - height_int // 2
            kiri_bottom = kiri_top + height_int
            kiri_img = img[kiri_top:kiri_bottom, kiri_left:kiri_right]
            cv2.imwrite(save_dir + '/' + str(count) + '.jpg', kiri_img)
            # cv2.imwrite(save_tmp_train_a + '/' + str(count) + '.jpg', kiri_img)
            # cv2.imwrite(save_tmp_train_b + '/' + str(count) + '.jpg', kiri_img)
            # cv2.imwrite(save_tmp_val_a + '/' + str(count) + '.jpg', kiri_img)
            # cv2.imwrite(save_tmp_val_b + '/' + str(count) + '.jpg', kiri_img)
            count += 1 