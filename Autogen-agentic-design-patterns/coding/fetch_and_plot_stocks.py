# filename: fetch_and_plot_stocks.py

from functions import get_stock_prices, plot_stock_prices

# Define stock symbols and dates
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-06-19'

# Fetch stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot and save the stock prices
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')