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
show_close = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False  # Convert "1"/"0" to True/False
period = n_years * 365

# Load data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data(TICKER)

# Plot raw data based on checkbox selections
def plot_raw_data(data, show_open, show_close):
    fig = go.Figure()
    if show_open:
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock Open', line=dict(color='lightgreen')))
    if show_close:
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close', line=dict(color='red')))
    fig.update_layout(
        title_text=TICKER.upper(),
        xaxis_rangeslider_visible=False,
        width=900,
        height=600,
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background for the plot area
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background for the entire figure
        font=dict(color='white')  # Text color can be adjusted for visibility
    )
    fig.write_html("C:/xampp/htdocs/asset/graph/raw_data_plot.html")
    print("Raw data plot saved as 'raw_data_plot.html'.")

plot_raw_data(data, show_open, show_close)

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

# Modify forecast plot to set marker color to white for the data points
fig1.update_traces(
    marker=dict(color='white', size=5)  # Set marker color to white and size to 5 (you can adjust the size)
)

fig1.update_layout(
    xaxis=dict(
        rangeslider=dict(visible=False),  # Keep the range slider off
        rangeselector=dict(
            buttons=[
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")  # Option to view all data
            ],
            font=dict(color="white"),  # Set text color of the range selector
            bgcolor="rgba(0, 0, 0, 0.5)",  # Background color for the range selector
            activecolor="deepskyblue"  # Active button color
        )
    ),
    width=900,
    height=600,
    plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background for the plot area
    paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent background for the entire figure
    font=dict(color="white")  # Set text color to white
)

# fig1.update_layout(
#     xaxis_rangeslider_visible=False,
#     width=900,
#     height=600,
#     plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background for the plot area
#     paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background for the entire figure
#     font=dict(color='white'),  # Set text color to white
# )    
    
fig1.write_html("C:/xampp/htdocs/asset/graph/forecast_plot.html")
print("Forecast plot saved as 'forecast_plot.html'.")


# The 'activecolor' property is a color and may be specified as:
#       - A hex string (e.g. '#ff0000')
#       - An rgb/rgba string (e.g. 'rgb(255,0,0)')
#       - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
#       - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
#       - A named CSS color:
#             aliceblue, antiquewhite, aqua, aquamarine, azure,
#             beige, bisque, black, blanchedalmond, blue,
#             blueviolet, brown, burlywood, cadetblue,
#             chartreuse, chocolate, coral, cornflowerblue,
#             cornsilk, crimson, cyan, darkblue, darkcyan,
#             darkgoldenrod, darkgray, darkgrey, darkgreen,
#             darkkhaki, darkmagenta, darkolivegreen, darkorange,
#             darkorchid, darkred, darksalmon, darkseagreen,
#             darkslateblue, darkslategray, darkslategrey,
#             darkturquoise, darkviolet, deeppink, deepskyblue,
#             dimgray, dimgrey, dodgerblue, firebrick,
#             floralwhite, forestgreen, fuchsia, gainsboro,
#             ghostwhite, gold, goldenrod, gray, grey, green,
#             greenyellow, honeydew, hotpink, indianred, indigo,
#             ivory, khaki, lavender, lavenderblush, lawngreen,
#             lemonchiffon, lightblue, lightcoral, lightcyan,
#             lightgoldenrodyellow, lightgray, lightgrey,
#             lightgreen, lightpink, lightsalmon, lightseagreen,
#             lightskyblue, lightslategray, lightslategrey,
#             lightsteelblue, lightyellow, lime, limegreen,
#             linen, magenta, maroon, mediumaquamarine,
#             mediumblue, mediumorchid, mediumpurple,
#             mediumseagreen, mediumslateblue, mediumspringgreen,
#             mediumturquoise, mediumvioletred, midnightblue,
#             mintcream, mistyrose, moccasin, navajowhite, navy,
#             oldlace, olive, olivedrab, orange, orangered,
#             orchid, palegoldenrod, palegreen, paleturquoise,
#             palevioletred, papayawhip, peachpuff, peru, pink,
#             plum, powderblue, purple, red, rosybrown,
#             royalblue, rebeccapurple, saddlebrown, salmon,
#             sandybrown, seagreen, seashell, sienna, silver,
#             skyblue, slateblue, slategray, slategrey, snow,
#             springgreen, steelblue, tan, teal, thistle, tomato,
#             turquoise, violet, wheat, white, whitesmoke,
#             yellow, yellowgreen
    
    
    
    
