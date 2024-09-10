import json
import base64
import os

from PIL import Image
import io

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QListWidget


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def base64encode_img(image_path):
    src_image = Image.open(image_path)
    output_buffer = io.BytesIO()
    src_image.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    return base64.b64encode(byte_data).decode('utf-8')


def get_image():  #打开单个文件

    file_name, filetype = QFileDialog.getOpenFileName(None, "打开文件", " . ", "图像文件(*.jpg *.png)")
    if file_name:
        img = QPixmap(file_name)
        return img,file_name
    else:
        return None,None

def get_folder_img_info():  #打开文件夹
    img_folder_path = QFileDialog.getExistingDirectory()
    ext_lst = ['.jpg', '.JPG', '.bmp']
    img_files_list = []
    curr_pic_path = None
    if img_folder_path == "":
        return None,None
    else:
        files_list = os.listdir(img_folder_path)
        for file_name in files_list:
            name_ext = os.path.splitext(file_name)
            # 加了一层过滤机制，确保都是图片。
            if name_ext[1] in ext_lst:
                img_files_list.append(os.path.join(img_folder_path,file_name))
        curr_pic_path = img_files_list[0]
        # 返回当前的图片的路径和图片列表
        return img_files_list,curr_pic_path


