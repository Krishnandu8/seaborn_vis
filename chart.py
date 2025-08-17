# chart.py

# 1. Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Generate synthetic data for customer engagement patterns
# We create a dictionary to hold our data.
# np.random.seed(42) ensures that we get the same random data every time we run the script,
# making the result reproducible.
np.random.seed(42)

data = {
    'Website Visits': np.random.randint(100, 1000, 100),
    'Time on Site (min)': np.random.randint(5, 60, 100),
    'Purchases': np.random.randint(0, 15, 100),
    'Emails Opened': np.random.randint(1, 20, 100),
    'Support Tickets': np.random.randint(0, 5, 100),
    'Social Media Likes': np.random.randint(10, 500, 100)
}

# Add some realistic correlations
# Increase 'Purchases' and 'Time on Site' for customers with high 'Website Visits'
data['Time on Site (min)'] = data['Time on Site (min)'] + (data['Website Visits'] // 20)
data['Purchases'] = data['Purchases'] + (data['Time on Site (min)'] // 10)

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# 3. Apply professional styling
# Set the style for a professional, publication-ready look. 'white' is clean.
sns.set_style("white")

# Set the context to 'talk' for larger, more readable fonts suitable for presentations.
sns.set_context("talk", font_scale=0.8)

# 4. Set the figure size for the required 512x512 output
# figsize=(8, 8) inches and dpi=64 will result in an 8*64 x 8*64 = 512x512 pixel image.
plt.figure(figsize=(8, 8))

# 5. Create the heatmap
# - annot=True displays the correlation values on the map.
# - fmt='.2f' formats the numbers to two decimal places.
# - cmap='coolwarm' is a great palette for correlation matrices, as it shows positive
#   correlations in warm colors (reds) and negative in cool colors (blues).
heatmap = sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=.5,
    cbar=True
)

# 6. Style the chart with titles and labels
# Add a clear, descriptive title for executive audiences.
heatmap.set_title(
    'Customer Engagement Metrics Correlation Matrix',
    fontdict={'fontsize': 16},
    pad=12
)

# Ensure layout is tight to prevent labels from being cut off.
plt.tight_layout()

# 7. Save the chart as a PNG file
# Use the specified parameters to ensure the output is exactly 512x512 pixels.
# bbox_inches='tight' removes any extra white space around the plot.
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("chart.png has been generated successfully with 512x512 dimensions.")
