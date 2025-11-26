from generate_page import generate_pages_recursively
from copy_to_public import copy_conetent
import sys

def main ():
    if len(sys.argv) > 2:
        basepath = sys.argv
    else:
        basepath = "/"
    copy_conetent("./static", "./docs")
    generate_pages_recursively("content", "template.html", "docs", basepath)

main()

