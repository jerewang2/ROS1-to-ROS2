import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def generate_rst_file(data):
    with open('output_file.rst', 'w') as file:
        for item in data:
            file.write(f".. _{item['ROS1_name']}:\n\n")
            file.write(f"{item['ROS1_name']} - {item['ROS1_description']}\n\n")
            file.write(f"Equivalent ROS2 code: {item['ROS2_code']}\n")
