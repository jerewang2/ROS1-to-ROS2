import csv
import re
import requests
import os

def process_permalink(permalink):
    permalink = re.sub(r'^https://github\.com/', 'https://raw.githubusercontent.com/', permalink)
    permalink = re.sub(r'/blob/', '/', permalink)

    match = re.search(r'#L(\d+)C\d+-L(\d+)C\d+', permalink)

    if match:
        start = int(match.group(1))
        end = int(match.group(2))

        permalink = re.sub(r'#L\d+C\d+-L\d+C\d+', '', permalink)

        response = requests.get(permalink)
        response.raise_for_status()
        lines_of_code = response.text.splitlines()

        snippet = lines_of_code[start - 1:end]
        snippet_text = "\n".join(snippet)

        return snippet_text
    else:
        return ""  # Fallback if the pattern doesn't match

def preprocess_csv(path):
    sections = []

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subsection = row['Name of Subsection'].strip()
            ros1_link = row['ROS1 Permalink'].strip()
            description = row['Description'].strip()

            ros1_code = process_permalink(ros1_link)

            sections.append((subsection, ros1_code, description))

    return sections

def generate_rst_file(sections):
    output_path = os.path.join("docs/source", "translation.rst")
    with open(output_path, 'w') as file:
        file.write("Translation\n")
        file.write("===========\n\n")

        for subsection, code, description in sections:
            anchor = subsection.lower().replace(' ', '-')
            file.write(f".. _{anchor}:\n\n")
            file.write(f"{subsection}\n")
            file.write(f"{'-' * len(subsection)}\n\n")
            file.write(f"{description}\n\n")
            file.write(".. code-block:: cpp\n\n")
            # Indent each line of code
            for line in code.splitlines():
                file.write(f"   {line}\n")
            file.write("\n")

def main():
    path = 'data.csv'
    sections = preprocess_csv(path)
    generate_rst_file(sections)

if __name__ == '__main__':
    main()
