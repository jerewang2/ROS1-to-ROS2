import csv
import requests
import re

def process_permalink(permalink):
    permalink = re.sub(r'^https://github\.com/', 'https://raw.githubusercontent.com/', permalink)
    permalink = re.sub(r'/blob/', '/', permalink)
    match = re.search(r'#L(\d+)C\d+-L(\d+)C\d+', permalink)

    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        permalink = re.sub(r'#L\d+C\d+-L\d+C\d+', '', permalink)

        response = requests.get(permalink)
        if response.status_code != 200:
            return f"# Failed to fetch code from: {permalink}"

        lines = response.text.splitlines()
        snippet = lines[start - 1:end]
        return "\n".join(f"{i+start} {line}" for i, line in enumerate(snippet))
    return "# Invalid permalink"

def preprocess_csv(csv_path):
    output = []
    output.append("Translation")
    output.append("=" * len("Translation"))
    output.append("")

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subsection = row['Name of Subsection']
            ros1_link = row['ROS1 Permalink']
            ros2_link = row['ROS2 Permalink']
            description = row['Description']

            anchor = subsection.lower().replace(" ", "_")
            output.append(f".. _{anchor}:\n")
            output.append(f"{subsection}")
            output.append("-" * len(subsection))
            output.append("")
            output.append(description)
            output.append("")

            output.append("ROS1 Example")
            output.append("")
            output.append(".. code-block:: console\n")
            ros1_code = process_permalink(ros1_link)
            output.append(indent_code(ros1_code))
            output.append("")

            output.append("ROS2 Example")
            output.append("")
            output.append(".. code-block:: console\n")
            ros2_code = process_permalink(ros2_link)
            output.append(indent_code(ros2_code))
            output.append("")

            output.append("=" * 11)
            output.append("")

    return "\n".join(output)

def indent_code(code):
    return "\n".join(f"   {line}" for line in code.splitlines())

def generate_rst_file(data):
    with open("docs/translation.rst", "w") as file:
        file.write(data)

if __name__ == "__main__":
    path = "data.csv"
    processed = preprocess_csv(path)
    generate_rst_file(processed)
