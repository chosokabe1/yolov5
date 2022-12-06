import cv2
import numpy as np
import os
import glob
from PIL import Image

def padding_0(path, min_size, out_path):
  img = cv2.imread(path)
  h, w, _ = img.shape
  flag = 0
  if h < min_size:
    newimg = np.zeros((min_size, w, 3))
    start = int((min_size - h) / 2)
    fin = int((min_size + h) / 2)
    newimg[start:fin, :] = img
    flag = 1
  
  if w < min_size:
    newimg = np.zeros((h, min_size, 3))
    start = int((min_size - w) / 2)
    fin = int((min_size + w) / 2)
    newimg[:, start:fin] = img
    flag = 1

  if flag == 1:
    file_name = os.path.splitext(os.path.basename(path))[0]
    cv2.imwrite(os.path.join(out_path, file_name + '.jpg'), newimg)
  else:
    file_name = os.path.splitext(os.path.basename(path))[0]
    cv2.imwrite(os.path.join(out_path, file_name + '.jpg'), img)

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def make_square_dir(in_dir_path, outpath):
  for imgpath in sorted(glob.glob(in_dir_path + "\*")):
    out_img_path = outpath + "\\" + os.path.basename(imgpath)
    im = Image.open(imgpath)
    print('7')
    im_new = expand2square(im, 0)
    im_new.save(out_img_path, quality=95)

def make_square_file(in_path, out_path):
  out_img_path = out_path + "\\" + os.path.basename(in_path)
  im = Image.open(in_path)
  im_new = expand2square(im, 0)
  im_new.save(out_img_path, quality=95)