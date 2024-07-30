import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('output.csv')

# Convert the 'time' column from UNIX timestamp to datetime
df['datetime'] = pd.to_datetime(df['time'], unit='s')

# Extract the interest values from the 'value' column
# Assuming 'value' column contains string representations of lists (e.g., "[77]")
df['interest'] = df['value'].apply(lambda x: int(x.strip('[]')))

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df['interest'], marker='o', linestyle='-', color='b')

# Adding title and labels
plt.title('Interest Over Time')
plt.xlabel('Time')
plt.ylabel('Interest')
plt.grid(True)

# Formatting x-axis for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
