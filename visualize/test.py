import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the CSV file
df = pd.read_csv('VIC (1).csv')  # Replace with your CSV file name
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Create the figure with subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.03, subplot_titles=('Candlestick', 'Volume'), 
                    row_width=[0.7, 0.3])

# Add candlestick trace
fig.add_trace(go.Candlestick(x=df['Date/Time'],
                             open=df['Open'],
                             high=df['High'],
                             low=df['Low'],
                             close=df['Close'],
                             name='Price'),
              row=1, col=1)

# Add volume bar trace
fig.add_trace(go.Bar(x=df['Date/Time'], y=df['Volume'], name='Volume'),
              row=2, col=1)

# Update layout
fig.update_layout(
    title='Interactive Stock Chart',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False,
    height=800,
    width=1200,
    showlegend=False
)

# Update y-axes
fig.update_yaxes(title_text='Price', row=1, col=1)
fig.update_yaxes(title_text='Volume', row=2, col=1)

# Show the plot
fig.show()