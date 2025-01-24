import sys
import yaml
import os
import frontmatter

def process_markdown_files(input_files, output_file):
    combined_data = {"kgs": []}
    for file in input_files:
        with open(file, "r") as f:
            doc = frontmatter.load(f)
            combined_data["kgs"].append(doc.metadata)

    # Sort the YAML data by keys
    combined_data["kgs"].sort(key=lambda x: yaml.dump(x, sort_keys=True))

    # Write the combined YAML to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        yaml.dump(combined_data, f, sort_keys=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combine_registry.py <output_file> <input_file1> [<input_file2> ...]")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    process_markdown_files(input_files, output_file)
