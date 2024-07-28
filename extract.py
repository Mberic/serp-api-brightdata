import json
import csv

# Load JSON data from a file
with open('response.json', 'r') as json_file:
    data = json.load(json_file)

# Define the fields to extract
fields_to_extract = ['title', 'rank']

# Function to filter a single dictionary
def filter_dict(d, fields):
    return {k: v for k, v in d.items() if k in fields}

# Extract the relevant part of the data
if isinstance(data["organic"], list):
    filtered_data = [filter_dict(item, fields_to_extract) for item in data["organic"]]
else:
    filtered_data = filter_dict(data["organic"], fields_to_extract)

# Define the CSV file name
csv_file_name = 'output.csv'

# Open the CSV file for writing
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header (fields to extract)
    csv_writer.writerow(fields_to_extract)

    # Write the rows (extracted field values)
    for item in filtered_data:
        row = [item[field] for field in fields_to_extract]
        csv_writer.writerow(row)

print(f"Data successfully written to {csv_file_name}")
