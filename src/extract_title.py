def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    h1_line = None
    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            h1_line = line
            break
    if h1_line is None:
        raise Exception("No h1 header found")
    return h1_line.lstrip("#").strip()

if __name__ == "__main__":
    print(extract_title("# Hello"))
    try:
        print(extract_title("## Not a title"))
    except Exception as e:
        print("raised:", e)