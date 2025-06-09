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

        try:
            response = requests.get(permalink)
            response.raise_for_status()
            lines_of_code = response.text.splitlines()
            snippet = lines_of_code[start - 1:end]
            return "\n".join(snippet)
        except Exception as e:
            print(f"Error fetching code from {permalink}: {e}")
            return ""
    else:
        print(f"Could not parse line numbers from permalink: {permalink}")
        return ""

def generate_rst_entry(subsection, description, ros1_code, ros2_code):
    return f"""
.. _{subsection.lower().replace(' ', '_')}:

{subsection}
{'-' * len(subsection)}

{description}

**ROS1 Example**

.. code-block:: console

{indent_code(ros1_code)}

**ROS2 Example**

.. code-block:: console

{indent_code(ros2_code)}

"""

def indent_code(code):
    return '\n'.join(f'   {line}' for line in code.splitlines())

def main():
    with open('translation.rst', 'w') as rstfile:
        rstfile.write("Translation\n===========\n\n")

        with open('translation_map.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                subsection = row['Name of Subsection'].strip()
                ros1_code = process_permalink(row['ROS1 Permalink'].strip())
                ros2_code = process_permalink(row['ROS2 Permalink'].strip())
                description = row['Description'].strip()

                rst_entry = generate_rst_entry(subsection, description, ros1_code, ros2_code)
                rstfile.write(rst_entry)

if __name__ == "__main__":
    main()
