import pandas as pd
import matplotlib.pyplot as plt

# Load data (Data Frames), parse dates to be able to plot
df = pd.read_csv("data/archive/PJM_Load_hourly.csv", parse_dates=["Datetime"], index_col="Datetime")

# Handle missing values (if any) (cleaning data, drop NA values)
df = df.dropna()  # Or use df.fillna(method="ffill")

print("First 5 rows of data:")
print(df.head())

print("Basic statistics:")
print(df.describe())

# plot everything and save the image
plt.figure(figsize=(10, 5))  # Creates a figure 10 inches wide, 5 inches tall
plt.plot(df["Datetime"], df["PJM_Load_MW"])  # Creates a line plot
plt.title("PJM Electricity Demand")  # Adds a title
plt.xlabel("Date")  # Labels the x-axis
plt.ylabel("Demand (MW)")  # Labels the y-axis
plt.xticks(rotation=45)  # Rotates x-axis labels for better readability
plt.tight_layout()  # Adjusts spacing
plt.savefig("plots/electricity_demand.png")  # Saves the plot as an image
