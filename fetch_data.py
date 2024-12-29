import yfinance as yf
import pandas as pd

# Fetch historical data for TTWO
symbol = "TTWO"
stock = yf.Ticker(symbol)
historical_data = stock.history(period="1y")  # 1 year of historical data

# Save historical data as CSV
historical_data.to_csv("historical_data.csv")

# Generate stock stats
stats = {
    "Symbol": symbol,
    "Market Cap": stock.info.get("marketCap"),
    "52 Week High": stock.info.get("fiftyTwoWeekHigh"),
    "52 Week Low": stock.info.get("fiftyTwoWeekLow"),
    "Dividend Yield": stock.info.get("dividendYield"),
}

# Create an HTML file for the stats
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{symbol} Stats</title>
</head>
<body>
    <h1>Stock Statistics for {symbol}</h1>
    <ul>
        {''.join(f'<li><strong>{key}:</strong> {value}</li>' for key, value in stats.items())}
    </ul>
    <h2>Historical Data</h2>
    <p>See the CSV file for detailed historical data.</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
