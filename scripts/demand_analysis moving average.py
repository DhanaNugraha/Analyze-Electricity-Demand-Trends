import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv(
    "data/archive/PJM_Load_hourly.csv", parse_dates=["Datetime"], index_col="Datetime"
)

# Calculate 7-day and 30-day moving averages
df["7_day_MA"] = (
    df["PJM_Load_MW"].rolling(window=7 * 24, min_periods=1).mean()
)  
# 7 days * 24 hours, since data is hourly
# min period will show a value even with less than 7 days of data, Without this, you'd see NaN for the first 167 hours
df["30_day_MA"] = (
    df["PJM_Load_MW"].rolling(window=30 * 24, min_periods=1).mean()
)  # 30 days * 24 hours

# Plot
plt.figure(figsize=(14, 7))
plt.plot(
    df.index, df["PJM_Load_MW"], label="Hourly Demand", alpha=0.3, color="lightgray"
)
plt.plot(df.index, df["7_day_MA"], label="7-Day Moving Average", color="blue")
plt.plot(
    df.index, df["30_day_MA"], label="30-Day Moving Average", color="red", linewidth=2
)

# Formatting
plt.title("Electricity Demand with Moving Averages", pad=20)
plt.xlabel("Date")
plt.ylabel("Demand (MW)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("plots/moving_average_demand.png")
plt.show()

# Print latest moving average values
# iloc = i location in list, [-1] last one
print(f"Latest 7-day MA: {df['7_day_MA'].iloc[-1]:.0f} MW")
print(f"Latest 30-day MA: {df['30_day_MA'].iloc[-1]:.0f} MW")
