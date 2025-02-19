import json
import csv

# Load JSON data from a file
with open('response.json', 'r') as json_file:
    data = json.load(json_file)

# Define the fields to extract
fields_to_extract = ['time', 'value']

# Function to filter a single dictionary
def filter_dict(d, fields):
    return {k: v for k, v in d.items() if k in fields}

# Extract the relevant part of the data
#
# Please note that you need to look at the JSON data 
# returned in the `response.json` file in order for you
# to know the different JSON fields of the scraped data

timelineData = data['widgets'][0]['data']['default']['timelineData']

if isinstance(timelineData, list):
    filtered_data = [filter_dict(item, fields_to_extract) for item in timelineData]
else:
    filtered_data = filter_dict(timelineData, fields_to_extract)

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
