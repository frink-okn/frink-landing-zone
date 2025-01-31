import sys
import yaml
import os
import frontmatter

def process_markdown_files(input_files, output_file):
    output = """
# OKN registry

## Knowledge graphs registered with the Open Knowledge Network

| Shortname | Title | Description |
| :-------- | :---- | :---------- |
"""
    # Write the combined YAML to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    for file in input_files:
        with open(file, "r") as f:
            doc = frontmatter.load(f)
            shortname = doc.metadata['shortname']
            output += f"| [{shortname}](kgs/{shortname}/) | {doc.metadata['title']} | {doc.metadata['description']} |\n"
    with open(output_file, "w") as f:
        f.write(output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_registry_index.py <output_file> <input_file1> [<input_file2> ...]")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    process_markdown_files(input_files, output_file)
