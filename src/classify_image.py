import os
import sys
import re
import shutil


src_directory = "/Users/shunrongshen/Downloads/output_vn"
tgt_directory = "data/orig-vn"


# Load files
def load_images(image_path):
    if os.path.isdir(image_path):
        return [f for f in os.listdir(image_path) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]
    else:
        return [image_path]

src_files = load_images(src_directory)
for src_file in src_files:
    user_id = re.match(r"(\d+)_\w+\.[jpg|jpeg|png]", src_file, re.I)[1]
    tgt_path = os.path.join(tgt_directory, user_id)
    if not os.path.isdir(tgt_path):
        os.makedirs(tgt_path)
    src_path = os.path.join(src_directory, src_file)
    shutil.copyfile(src_path, os.path.join(tgt_path, src_file))
