import os
from block import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f_content = open(from_path)
    content = f_content.read()
    f_template = open(template_path)
    template = f_template.read()
    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', f"href=\"{basepath}")
    template = template.replace('src="/', f"src=\"{basepath}")
    with open (dest_path, "w") as f:
        f.write(template)
    f_content.close()
    f_template.close()

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    all_content = os.listdir(dir_path_content)
    for content in all_content:
        joined_content_path = os.path.join(dir_path_content, content)
        if content.endswith(".md"):
            final_html_file = f"{content.strip('.md')}.html"
            final_dest = os.path.join(dest_dir_path, final_html_file)
            generate_page(joined_content_path, template_path, final_dest, basepath)
        elif os.path.isdir(joined_content_path):
            final_dir = os.path.join(dest_dir_path, content)
            os.mkdir(final_dir)
            generate_pages_recursively(joined_content_path, template_path, final_dir, basepath)
        else:
            continue
