from generate_page import generate_pages_recursively
from copy_to_public import copy_conetent
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main ():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_conetent(dir_path_static, dir_path_public)
    generate_pages_recursively(dir_path_content, template_path, dir_path_public, basepath)

main()

