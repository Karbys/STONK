import sys
import yfinance as yf
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Define constants
START = "2012-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Get command-line arguments (ticker and years)
TICKER = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
n_years = int(sys.argv[2]) if len(sys.argv) > 2 else 1
period = n_years * 365

# Load data from yfinance
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data(TICKER)

# Plot raw data and save as HTML
def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close', line=dict(color='red')))
    fig.update_layout(title_text="Time Series Data", xaxis_rangeslider_visible=True, width=900, height=600)
    fig.write_html("D:/xampp/htdocs/asset/graph/raw_data_plot.html")
    print("Raw data plot saved as 'raw_data_plot.html'.")

plot_raw_data(data)

# Prepare data for Prophet model
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Train Prophet model and make future predictions
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Save forecast plot as HTML
fig1 = plot_plotly(m, forecast)
fig1.update_layout(width=900, height=600)
fig1.write_html("D:/xampp/htdocs/asset/graph/forecast_plot.html")
print("Forecast plot saved as 'forecast_plot.html'.")

# Save forecast components plot as PNG
fig2 = m.plot_components(forecast)
fig2.savefig("D:/xampp/htdocs/asset/img/forecast_components.png")
print("Forecast components plot saved as 'forecast_components.png'.")
