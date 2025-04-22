import csv
import pandas as pd

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
    print(df.head())