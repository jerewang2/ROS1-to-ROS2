import csv
import requests
import re

def process_permalink(permalink):
    permalink = re.sub(r'https://github.com/', 'https://raw.githubusercontent.com/', permalink)
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
            ros1_links = row['ROS1 Permalink'].split('|')  # Split by delimiter
            ros2_links = row['ROS2 Permalink'].split('|')  # Split by delimiter
            description = row['Description']

            anchor = subsection.lower().replace(" ", "_")
            output.append(f".. _{anchor}:\n")
            output.append(f"{subsection}")
            output.append("-" * len(subsection))
            output.append("")
            output.append(description)
            output.append("")

            # Process ROS1 permalinks
            output.append("ROS1 Example")
            output.append("")
            ros1_code_blocks = []
            for link in ros1_links:
                if link.strip():  # Skip empty links
                    ros1_code_blocks.append(process_permalink(link.strip()))
            
            if ros1_code_blocks:
                output.append(".. code-block:: console\n")
                for i, code_block in enumerate(ros1_code_blocks):
                    if i > 0:  # Add separator between multiple code blocks
                        output.append("")
                        output.append(".. code-block:: console\n")
                    output.append(indent_code(code_block))
            output.append("")

            # Process ROS2 permalinks
            output.append("ROS2 Example")
            output.append("")
            ros2_code_blocks = []
            for link in ros2_links:
                if link.strip():  # Skip empty links
                    ros2_code_blocks.append(process_permalink(link.strip()))
            
            if ros2_code_blocks:
                output.append(".. code-block:: console\n")
                for i, code_block in enumerate(ros2_code_blocks):
                    if i > 0:  # Add separator between multiple code blocks
                        output.append("")
                        output.append(".. code-block:: console\n")
                    output.append(indent_code(code_block))
            output.append("")

            output.append("=" * 11)
            output.append("")

    return "\n".join(output)

def indent_code(code):
    return "\n".join(f"   {line}" for line in code.splitlines())

def generate_rst_file(data):
    # Explicitly clear the file first
    with open("docs/source/translation.rst", "w") as file:
        file.truncate(0)
    # Now write the new data
    with open("docs/source/translation.rst", "w") as file:
        file.write(data)

if __name__ == "__main__":
    path = "data.csv"
    processed = preprocess_csv(path)
    generate_rst_file(processed)
