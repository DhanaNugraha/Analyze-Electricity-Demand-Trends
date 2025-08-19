import pandas as pd
import matplotlib.pyplot as plt

# Load data (Data Frames), parse dates to be able to plot
df = pd.read_csv("data/archive/PJM_Load_hourly.csv", parse_dates=["Datetime"], index_col="Datetime")

# Add day of week (0=Monday, 6=Sunday) and hour columns
df['day_of_week'] = df.index.dayofweek  # Monday=0, Sunday=6
df['hour'] = df.index.hour

# Create a new column for weekday/weekend
df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Calculate hourly averages for weekdays and weekends
hourly_avg = df.groupby(['day_type', 'hour']).mean()['PJM_Load_MW'].unstack(level=0)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(hourly_avg.index, hourly_avg['Weekday'], label='Weekday', linewidth=2)
plt.plot(hourly_avg.index, hourly_avg['Weekend'], label='Weekend', linewidth=2)

# Formatting
plt.title('Average Hourly Electricity Demand: Weekday vs Weekend', pad=20)
plt.xlabel('Hour of Day')
plt.ylabel('Average Demand (MW)')
plt.xticks(range(0, 24)) #To make sure hour 0 until 24 are shown
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig('plots/weekday_vs_weekend.png')
plt.show()

# Print some statistics
print("Peak Hours:")
print(
    f"Weekday: {hourly_avg['Weekday'].idxmax()}:00 - {hourly_avg['Weekday'].max():.0f} MW" 
) #idxmax for x axis that have max value, max for max value in y
print(
    f"Weekend: {hourly_avg['Weekend'].idxmax()}:00 - {hourly_avg['Weekend'].max():.0f} MW"
)

print("\nDaily Averages:")
# .mean for the day type
print(f"Weekday: {df[df['day_type'] == 'Weekday']['PJM_Load_MW'].mean():.0f} MW")
print(f"Weekend: {df[df['day_type'] == 'Weekend']['PJM_Load_MW'].mean():.0f} MW")