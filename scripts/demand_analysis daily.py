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

print("95% percentile")
print(df.quantile(0.95)) #this is the 95th percentile of the data with description

print("95% percentile 2")
print(df["PJM_Load_MW"].quantile(0.95)) #this is the 95th percentile of the data but only the number

print("Dailies")
daily_load = df.resample("D").mean()
print(daily_load.head())

print("Weekly")
weekly_load = df.resample("W").mean()
print(weekly_load.head())

print("Monthly")
monthly_load = df.resample("M").mean()
print(monthly_load.head())


# plots daily and displays
plt.figure(figsize=(12, 6))
plt.plot(daily_load.index, daily_load["PJM_Load_MW"], label="Daily Demand")
plt.title("PJM Daily Electricity Demand")
plt.xlabel("Date")
plt.ylabel("Load (MW)")
plt.grid()
plt.legend() 
plt.show() #shows plot but not saving

