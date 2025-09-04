from pathlib import Path
from extract_title import extract_title
from markdown_blocks import markdown_to_html_node  # you wrote this earlier

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = Path(dest_path).parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page_html)