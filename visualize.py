import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('output.csv')

# Display the first few rows of the DataFrame to verify the data
print(df.head())

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(df['title'], df['rank'], color='skyblue')
plt.xlabel('Rank')
plt.ylabel('Title')
plt.title('Rank of Pizza-Related Titles')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest rank at the top
plt.show()
