import os
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)

save_tmp_train_a = "runs/detect/egg_or_not/tmp/train/a"
makedir(save_tmp_train_a)
save_tmp_train_b = "runs/detect/egg_or_not/tmp/train/b"
makedir(save_tmp_train_b)
save_tmp_val_a = "runs/detect/egg_or_not/tmp/val/a"
makedir(save_tmp_val_a)
save_tmp_val_b = "runs/detect/egg_or_not/tmp/val/b"
makedir(save_tmp_val_b)
from classification_module import makesquare
makesquare.make_square_file("runs/detect/egg_or_not/microbial_region/0.jpg", out_path=save_tmp_train_a)
makesquare.make_square_file("runs/detect/egg_or_not/microbial_region/0.jpg", out_path=save_tmp_train_b)
makesquare.make_square_file("runs/detect/egg_or_not/microbial_region/0.jpg", out_path=save_tmp_val_a)
makesquare.make_square_file("runs/detect/egg_or_not/microbial_region/0.jpg", out_path=save_tmp_val_b)