import sys
import yfinance as yf
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Constants
START = "2012-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Get command-line arguments
TICKER = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
n_years = int(sys.argv[2]) if len(sys.argv) > 2 else 1
show_open = bool(int(sys.argv[3])) if len(sys.argv) > 3 else False  # Convert "1"/"0" to True/False
period = n_years * 365

# Load data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data(TICKER)

# Function to create an empty graph
def plot_empty_graph(title, file_name):
    fig = go.Figure()
    fig.update_layout(
        title_text=title,
        xaxis=dict(title='Date', range=['2012-01-01', TODAY]),
        yaxis=dict(title='Value', range=[0, 1]),
        width=900,
        height=600,
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        font=dict(color='white')  # Text color
    )
    fig.write_html(file_name)
    print(f"Empty graph saved as '{file_name}'.")

# Check if data is available
if data.empty:
    print(f"No data available for ticker '{TICKER}'. Plotting empty graphs.")
    plot_empty_graph(f"{TICKER.upper()} Raw Data (No Data Available)", "D:/xampp/htdocs/asset/graph/raw_data_plot.html")
    plot_empty_graph(f"{TICKER.upper()} Forecast (No Data Available)", "D:/xampp/htdocs/asset/graph/forecast_plot.html")
else:
    # Plot raw data
    def plot_raw_data(data):
        fig = go.Figure()

        # Add line for Close price with filled area under the line
        fig.add_trace(go.Scatter(
            x=data['Date'],
            y=data['Close'],
            mode='lines',
            name='<b>Date</b>',
            line=dict(color='lightgreen'),
            fill='tozeroy',  # Fill the area below the line with the same color
            fillcolor='rgba(144, 238, 144, 0.3)',  # Light green with some transparency
            hovertemplate=(
                "%{x|%d %B %Y}<br>"  # Format: Day Month Year (e.g., 01 January 2024)
                "<b>Close:</b> %{y:.2f} USD<br>"
                "<b>Open:</b> %{customdata[0]:.2f} USD<br>"
                "<b>High:</b> %{customdata[1]:.2f} USD<br>"
                "<b>Low:</b> %{customdata[2]:.2f} USD<br>"
                "<b>Volume:</b> %{customdata[3]:,}<br>"
            ),
            customdata=data[['Open', 'High', 'Low', 'Volume']].values,
            hoverlabel=dict(
                bgcolor="black",  # Set background color to black
                font=dict(color="white")  # Set text color to white
            )
        ))

        # Customize layout
        fig.update_layout(
            title_text=f"{TICKER.upper()} Stock Prices",
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            template="plotly_dark",
            hovermode="x unified",  # Hover over the entire line
            width=900,
            height=600,
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background
            font=dict(color="white"),  # Text color
            hoverlabel=dict(
                bgcolor="black",  # Set background color to black
                font=dict(color="white")  # Set text color to white
            ),
            xaxis=dict(
                rangeslider=dict(visible=False),  # Add a range slider for interactive zooming
                showgrid=True,  # Enable grid for better readability
                zeroline=False,  # Remove the x-axis zero line
            ),
            yaxis=dict(
                showgrid=True,  # Enable grid for better readability
                zeroline=False,  # Remove the y-axis zero line
            )
        )


        # Save the chart
        fig.write_html("D:/xampp/htdocs/asset/graph/raw_data_plot.html")
        print("Raw data plot saved as 'raw_data_plot.html'.")

# Call the function to plot raw data
plot_raw_data(data)

# Prepare data for Prophet
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Train and predict with Prophet
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Save forecast plot
fig1 = plot_plotly(m, forecast)

# Add line for Close price with filled area under the line
fig1.add_trace(go.Scatter(
    x=data['Date'],
    y=data['Close'],
    mode='lines',
    name='<b>Date</b>',
    line=dict(color='orange'),
    fill='tozeroy',  # Fill the area below the line with the same color
    fillcolor='rgba(255, 165, 0, 0.2)',  # Light green with some transparency
    hovertemplate=(
        "%{x|%d %B %Y}<br>"  # Format: Day Month Year (e.g., 01 January 2024)
        "<b>Close:</b> %{y:.2f} USD<br>"
        "<b>Open:</b> %{customdata[0]:.2f} USD<br>"
        "<b>High:</b> %{customdata[1]:.2f} USD<br>"
        "<b>Low:</b> %{customdata[2]:.2f} USD<br>"
        "<b>Volume:</b> %{customdata[3]:,}<br>"
    ),
    customdata=data[['Open', 'High', 'Low', 'Volume']].values,
    
))

# Add actual data points (historical data) as markers
# fig1.add_trace(go.Scatter(
#     x=df_train['ds'],
#     y=df_train['y'],
#     mode='markers',
#     marker=dict(color='white', size=3, line=dict(color='black', width=1)),  # Red points with black border
#     name='Actual Data'
# ))

# Update layout settings
fig1.update_layout(
    title_text=f"{TICKER.upper()} Stock Price Forecast",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_dark",
    hovermode="x unified",  # Hover over the entire line
    width=900,
    height=600,
    plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background
    paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background
    font=dict(color="white"),  # Text color
    hoverlabel=dict(
        bgcolor="black",  # Set background color to black
        font=dict(color="white")  # Set text color to white
    ),
    xaxis=dict(
        rangeslider=dict(visible=False),  # Add a range slider for interactive zooming
        rangeselector=dict(visible=False),  # Disable range selector for more clarity
        showgrid=True,  # Enable grid for better readability
        zeroline=False,  # Remove the x-axis zero line
    ),
    yaxis=dict(
        showgrid=True,  # Enable grid for better readability
        zeroline=False,  # Remove the y-axis zero line
    )
)

# Save the forecast chart
fig1.write_html("D:/xampp/htdocs/asset/graph/forecast_plot.html")
print("Forecast plot saved as 'forecast_plot.html'.")
