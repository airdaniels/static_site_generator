"""import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")"""

import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node  # Assuming this function works correctly


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * Generating page from {from_path} to {dest_path} using {template_path}")

    # Verify source files
    if not os.path.exists(from_path):
        print(f"Error: Markdown file '{from_path}' does not exist.")
        return
    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' does not exist.")
        return

    # Read the markdown file contents
    with open(from_path, 'r', encoding='utf-8') as from_file:
        markdown_content = from_file.read()
    print(f" * Markdown content:\n{markdown_content}")

    # Read the template file contents
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    print(f" * Template content:\n{template_content}")

    # Convert markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    print(f" * HTML content:\n{html_content}")

    # Extract the title using `extract_title` functions
    title = extract_title(markdown_content)
    print(f" * Extracted title: {title}")

    # Replace placeholders in the template with the title and content
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    print(f" * Final HTML content to be written:\n{final_content}")

    # Ensure the destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)

    # Write the final content to the destination file
    with open(dest_path, 'w', encoding='utf-8') as to_file:
        to_file.write(final_content)

    print(f" * Successfully generated page at {dest_path}")

                                                                                                                                    # Function to extract the title from the markdown content
def extract_title(md_content):
    lines = md_content.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError
