start python gpu_monitor.py 20
echo "Start all time |%date% %time%|"
call python clean_runs_detect.py
call python detect.py --weights runs\train\all\weights\last.pt --save-txt --img 640 --name egg_or_not --exist-ok --conf 0.1 --source C:\ex\sen\data\pickup_8times\img\07290845_1_100\07290845_1_100_00.jpg
echo "Finish YOLO time |%date% %time%|"
call python microbial_region_trimming.py C:\ex\sen\data\pickup_8times\img\07290845_1_100\07290845_1_100_00.jpg
call python save_square.py
call python is_it_egg.py
echo "Finish Effi time |%date% %time%|"
