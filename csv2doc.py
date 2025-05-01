import csv
import pandas as pd
import requests # type: ignore
import re

# def read_csv(file_path):
#     data = []
#     with open(file_path, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)
#     return data

def generate_rst_file(data):
    with open('translation.rst', 'w') as file:
        rst_content = f"""Translation
        ===========
        
        .. _publishers:

        {data[0]}
        -----------

        ROS1 Example

        .. code-block:: console"""

        file.write(f"{data[1]}\n")
        file.write(f"Description: {data[2]}")

def hello_world():
    print("Hello World!")

def preprocess_csv(file_path):
    df = pd.read_csv(file_path)
    
    for index, row in df.iterrows():
        subsection = row['Name of Subsection']
        ros1_link1 = row['ROS1 Permalink']
        ros2_link2 = row['ROS2 Permalink']
        description = row['Description']

        final = process_permalink(ros1_link1)

        return subsection, final, description

def process_permalink(permalink):
    permalink = re.sub(r'^https://github\.com/', 'https://raw.githubusercontent.com/', permalink)
    permalink = re.sub(r'/blob/', '/', permalink)

    match = re.search(r'#L(\d+)C\d+-L(\d+)C\d+', permalink)

    print(f'Permalink: {permalink}')
    print(f'Match: {match}')
    if match:
        start = int(match.group(1))
        end = int(match.group(2))

        print(f'Start: {start}, End: {end}')

        permalink = re.sub(r'#L\d+C\d+-L\d+C\d+', '', permalink)

        print(f'New permalink: {permalink}')

        lines_of_code = requests.get(permalink).text.splitlines()

        print(f'Lines of code: {lines_of_code}')

        snippet = lines_of_code[start - 1:end]
        snippet_text = "\n".join(snippet)

        print(f'Snippet: {snippet_text}')

        snippet_text = '#include <dynamic_reconfigure/server.h>\n#include <geometry_msgs/PoseStamped.h>\n#include <kr_mav_controllers/SO3Config.h>'

        return snippet_text