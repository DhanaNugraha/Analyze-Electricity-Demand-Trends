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

# make a new hour column by extracting hour from datetime column
df["hour"] = df.index.hour

# calculate hourly means, this one already have its own index because of groupby
hourly_means = df.groupby("hour").mean()

# plot
plt.figure(figsize=(10,5))
# hourly_means["PJM_Load_MW"].plot(kind="bar", color="blue") -> can like this
plt.bar(hourly_means.index, hourly_means["PJM_Load_MW"], color="blue") # better
plt.title("Average Hourly Electricity Demand")
plt.xlabel("Hour of Day")
plt.ylabel("Load (MW)")
plt.xticks(rotation=0)
plt.show()

