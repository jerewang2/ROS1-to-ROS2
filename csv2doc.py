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

        .. code-block:: console

            {data[1]}

        ===========
        
        {data[2]}
        """

        file.write(rst_content)

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

    if match:
        start = int(match.group(1))
        end = int(match.group(2))

        permalink = re.sub(r'#L\d+C\d+-L\d+C\d+', '', permalink)

        lines_of_code = requests.get(permalink).text.splitlines()

        snippet = lines_of_code[start - 1:end]
        snippet_text = "\n".join(snippet)

        snippet_text = '1 #include <dynamic_reconfigure/server.h>2 #include <geometry_msgs/PoseStamped.h>3 #include <kr_mav_controllers/SO3Config.h>'

        return snippet_text