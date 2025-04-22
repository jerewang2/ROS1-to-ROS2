import csv
import pandas as pd
import requests

# def read_csv(file_path):
#     data = []
#     with open(file_path, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)
#     return data

# def generate_rst_file(data):
#     with open('translation.rst', 'w') as file:
#         for item in data:
#             file.write(f"{item}:\n")

def hello_world():
    print("Hello World!")

def preprocess_csv(file_path):
    df = pd.read_csv(file_path)
    
    for index, row in df.iterrows():
        subsection = row['Name of Subsection']
        ros1_link1 = row['ROS1 Permalink']
        ros2_link2 = row['ROS2 Permalink']
        description = row['Description']

        code1 = requests.get(ros1_link1).text
        code2 = requests.get(ros2_link2).text

        print(f'Index: {index}')
        print(f'Subsection: {subsection}')
        print(f'Description: {description}')
        print(f'ros1 link: {code1}')
        print(f'ros2 link: {code2}')
        