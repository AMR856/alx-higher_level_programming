#!/usr/bin/python3
import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Jane', 30, 'Los Angeles'],
    ['Bob', 22, 'Chicago']
]

# Specify the file name and mode ('w' for write)
file_name = 'data.csv'

# Writing to CSV file
with open(file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f'Data has been serialized to {file_name}')