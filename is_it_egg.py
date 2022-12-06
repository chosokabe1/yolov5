from classification_module import val_model
from classification_module import finetuning_hy
import torch
from classification_module import modules
import torch.optim as optim
import os
import time

if __name__ == '__main__':
  output_name = "hoge"
  output_base_dir = "runs\\train"
  out_dir = os.path.join(output_base_dir,output_name)
  time_sta = time.time()
  model, input_size = finetuning_hy.initialize_model(model_name="efficientnetv2m", num_classes=2,  feature_extract=False, use_pretrained=True)
  model.load_state_dict(torch.load("..\\finetuning\\runs\\train\max_square_v2m\model_weights.pth"))
  dataloaders_dict, class_names = modules.data_load(input_size=input_size,data_dir="runs\detect\egg_or_not\\tmp", batch_size=1)

  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  model = model.to(device)
  time_end = time.time()
  load_time = time_end - time_sta
  time_sta = time.time()
  val_model.val(model=model, dataloaders=dataloaders_dict, class_names=class_names,out_dir=out_dir)
  time_end = time.time()
  val_time = time_end - time_sta

  print(f'ロード時間:{load_time}')
  print(f'推論時間{val_time}')