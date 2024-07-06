# filename: create_ytd_stock_plot.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for NVDA and TSLA from the start of the year to today
start_date = '2024-01-01'
end_date = '2024-06-19'
nvda = yf.download('NVDA', start=start_date, end=end_date)
tsla = yf.download('TSLA', start=start_date, end=end_date)

# Calculate the YTD gain as percentage
nvda['Gain'] = (nvda['Close'] / nvda['Close'].iloc[0] - 1) * 100
tsla['Gain'] = (tsla['Close'] / tsla['Close'].iloc[0] - 1) * 100

# Create a new plot
plt.figure(figsize=(10, 5))

# Plotting both datasets
plt.plot(nvda.index, nvda['Gain'], label='NVIDIA', color='blue')
plt.plot(tsla.index, tsla['Gain'], label='Tesla', color='red')

# Adding titles and labels
plt.title('YTD Stock Gains of NVIDIA and Tesla')
plt.xlabel('Date')
plt.ylabel('YTD Gain (%)')

# Display the legend
plt.legend()

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')
plt.show()