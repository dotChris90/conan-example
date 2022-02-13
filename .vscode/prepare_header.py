#!python3
from distutils.command import build
from logging import shutdown
from pathlib import Path
import os
import shutil

def mergefolders(root_src_dir, root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)


build_dir = Path(__file__).parent.parent.joinpath("build")

build_dir.joinpath("include").absolute().mkdir(exist_ok=True)

items = os.listdir(
    build_dir.absolute()
)

for item in items:
    if item == "include":
        pass
    else:
        dir_idx = build_dir.joinpath(item)
        if os.path.isdir(dir_idx.absolute()):
            inc_idx = dir_idx.joinpath("include")
            if os.path.isdir(inc_idx.absolute()) and os.path.exists(inc_idx.absolute()):
                mergefolders(str(inc_idx.absolute()),str(build_dir.joinpath("include").absolute()))