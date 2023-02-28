import pathlib
# 获取指定文件夹路径
folder_path = pathlib.Path(r'D:\Dataset\DOTA_vehicle\val_crop_600\labeltxt')
# 获取文件夹内所有文件的名称
file_list = [str(file_name) for file_name in folder_path.iterdir()]
# 保存文件名称到txt文件
with open('val.txt', 'w') as f:
    for file_name in file_list:
        f.write(file_name[-19:-4] + '\n')