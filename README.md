# Electricity Demand Analysis Project

🔍 **Project Overview**  
This project analyzes hourly electricity demand data from PJM Interconnection to identify consumption patterns, trends, and insights. The analysis is implemented in Python using Pandas for data manipulation and Matplotlib for visualization.

## 📁 Project Structure
Analyze-Electricity-Demand-Trends/
├── data/
│   └── archive/
│       ├── PJM_Load_hourly.csv  # Main dataset
│       └── ... (additional regional data files)
├── scripts/
│   ├── demand_analysis.py          # Basic analysis and visualization
│   ├── demand_analysis_daily.py    # Daily demand patterns
│   ├── demand_analysis_moving_average.py  # Moving average analysis
│   ├── demand_analysis_peak_hours.py      # Peak demand analysis
│   └── demand_analysis_weekday_vs_weekend.py  # Weekend vs weekday comparison
├── plots/  
│   ├── electricity_demand.png
│   ├── moving_average_demand.png
│   └── weekday_vs_weekend.png
└── README.md

## 📊 Analysis Scripts

### 1. Basic Analysis (`demand_analysis.py`)
- Loads and explores the hourly electricity demand data
- Provides basic statistics and data overview
- Visualizes raw hourly demand patterns

### 2. Daily Demand Analysis (`demand_analysis_daily.py`)
- Resamples data to daily, weekly, and monthly frequencies
- Calculates key statistics including 95th percentile
- Plots daily demand trends

### 3. Moving Average Analysis (`demand_analysis_moving_average.py`)
- Computes 7-day and 30-day moving averages
- Visualizes trends with moving average smoothing
- Helps identify long-term patterns and seasonality

### 4. Peak Hours Analysis (`demand_analysis_peak_hours.py`)
- Identifies peak demand hours
- Analyzes daily and seasonal peak patterns
- Helps in understanding load profiles

### 5. Weekday vs Weekend Analysis (`demand_analysis_weekday_vs_weekend.py`)
- Compares electricity consumption patterns between weekdays and weekends
- Identifies differences in demand profiles
- Useful for demand response planning

## 🛠️ Dependencies
- Python 3.x
- pandas
- matplotlib
- numpy

## 🚀 Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run individual analysis scripts from the `scripts/` directory
4. Generated plots will be saved in the `plots/` directory

## 📈 Key Insights
- **Daily Patterns**: Clear daily demand cycles with morning and evening peaks
- **Weekly Patterns**: Noticeable difference between weekday and weekend demand profiles
- **Seasonal Trends**: Higher demand in extreme weather months (summer and winter)
- **Peak Demand**: Occurs typically in late afternoon on weekdays

## 📝 Notes
- All scripts include error handling for missing data
- Plots are saved in high-resolution PNG format
- Scripts are well-commented for easy understanding and modification