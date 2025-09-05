# python
import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import *

dir_path_static = "./static"
dir_path_public = "./docs"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Using basepath: {basepath}")
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive("content", "template.html", "docs", basepath=basepath)

if __name__ == "__main__":
    main()