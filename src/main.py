from generate_page import generate_pages_recursively
from copy_to_public import copy_conetent

def main ():
    copy_conetent("./static", "./public")
    generate_pages_recursively("content", "template.html", "public")

main()

