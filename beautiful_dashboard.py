import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("🎨 CREATING BEAUTIFUL DASHBOARD")
print("="*60)

# Read the dataset
df = pd.read_csv('airlines_flights_data.csv')

# 1. MAIN DASHBOARD WITH PROPER SUBPLOT SPECIFICATIONS
print("📊 Creating Main Dashboard...")

# Create a comprehensive dashboard with proper specs
fig_main = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Price Distribution by Airline',
        'Route Popularity Heatmap',
        'Price vs Duration Analysis',
        'Market Share by Airline',
        'Booking Patterns by Days Left',
        'Price Analysis by Stops'
    ),
    specs=[
        [{"type": "box"}, {"type": "heatmap"}],
        [{"type": "scatter"}, {"type": "pie"}],
        [{"type": "bar"}, {"type": "violin"}]
    ]
)

# 1. Price distribution by airline (box plot)
for airline in df['airline'].unique():
    airline_data = df[df['airline'] == airline]['price']
    fig_main.add_trace(
        go.Box(y=airline_data, name=airline, boxpoints='outliers'),
        row=1, col=1
    )

# 2. Route popularity heatmap
route_matrix = df.groupby(['source_city', 'destination_city']).size().unstack(fill_value=0)
fig_main.add_trace(
    go.Heatmap(z=route_matrix.values, x=route_matrix.columns, y=route_matrix.index,
               colorscale='Viridis', name='Route Popularity'),
    row=1, col=2
)

# 3. Price vs Duration scatter
sample_df = df.sample(2000)
fig_main.add_trace(
    go.Scatter(x=sample_df['duration'], y=sample_df['price'], mode='markers',
               marker=dict(size=3, opacity=0.6, color=sample_df['days_left'], colorscale='Viridis'),
               name='Price vs Duration'),
    row=2, col=1
)

# 4. Market share pie chart
market_share = df['airline'].value_counts()
fig_main.add_trace(
    go.Pie(labels=market_share.index, values=market_share.values,
           hole=0.4, textinfo='label+percent'),
    row=2, col=2
)

# 5. Booking patterns by days left
days_bins = pd.cut(df['days_left'], bins=[0, 7, 14, 30, 49], labels=['1-7', '8-14', '15-30', '31-49'])
booking_patterns = df.groupby(days_bins)['price'].mean()
fig_main.add_trace(
    go.Bar(x=booking_patterns.index.astype(str), y=booking_patterns.values,
           name='Booking Patterns', marker_color='orange'),
    row=3, col=1
)

# 6. Price analysis by stops
for stop_type in df['stops'].unique():
    stop_data = df[df['stops'] == stop_type]['price']
    fig_main.add_trace(
        go.Violin(y=stop_data, name=stop_type, box_visible=True, meanline_visible=True),
        row=3, col=2
    )

fig_main.update_layout(
    height=1200,
    title_text="🚀 Airlines Data Analysis Dashboard",
    template='plotly_white',
    showlegend=True,
    title_font_size=24
)
fig_main.write_html('main_dashboard.html')

# 2. ADVANCED PRICE ANALYSIS
print("💰 Creating Advanced Price Analysis...")

fig_price = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Price Distribution with Normal Fit',
        'Price by Class and Airline',
        'Price Trends by Days Left',
        'Price Volatility Analysis'
    ),
    specs=[[{"secondary_y": True}, {"type": "box"}],
           [{"type": "scatter"}, {"type": "bar"}]]
)

# Price distribution with normal fit
price_data = df['price']
mu, sigma = stats.norm.fit(price_data)
x = np.linspace(price_data.min(), price_data.max(), 100)
y = stats.norm.pdf(x, mu, sigma)

fig_price.add_trace(
    go.Histogram(x=price_data, nbinsx=50, name='Actual', opacity=0.7, marker_color='lightblue'),
    row=1, col=1
)
fig_price.add_trace(
    go.Scatter(x=x, y=y*len(price_data)*50, name='Normal Fit', line=dict(color='red')),
    row=1, col=1, secondary_y=True
)

# Price by class and airline
for travel_class in df['class'].unique():
    class_data = df[df['class'] == travel_class]['price']
    fig_price.add_trace(
        go.Box(y=class_data, name=travel_class, boxpoints='outliers'),
        row=1, col=2
    )

# Price trends by days left
days_price = df.groupby('days_left')['price'].agg(['mean', 'std']).reset_index()
fig_price.add_trace(
    go.Scatter(x=days_price['days_left'], y=days_price['mean'], 
               mode='lines+markers', name='Average Price',
               line=dict(color='blue', width=3)),
    row=2, col=1
)

# Price volatility by route
route_volatility = df.groupby(['source_city', 'destination_city'])['price'].std().sort_values(ascending=False).head(10)
fig_price.add_trace(
    go.Bar(x=[f"{route[0]}→{route[1]}" for route in route_volatility.index], 
           y=route_volatility.values, name='Price Volatility'),
    row=2, col=2
)

fig_price.update_layout(
    height=800,
    title_text="💰 Advanced Price Analysis",
    template='plotly_white',
    showlegend=True
)
fig_price.write_html('advanced_price_dashboard.html')

# 3. INTERACTIVE TIME ANALYSIS
print("⏰ Creating Time Analysis Dashboard...")

fig_time = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Departure Time Preferences',
        'Price by Departure Time',
        'Duration vs Days Left',
        'Time-based Price Trends'
    )
)

# Departure time preferences
time_counts = df['departure_time'].value_counts()
fig_time.add_trace(
    go.Bar(x=time_counts.index, y=time_counts.values, name='Flight Count', marker_color='orange'),
    row=1, col=1
)

# Price by departure time
time_prices = df.groupby('departure_time')['price'].mean()
fig_time.add_trace(
    go.Bar(x=time_prices.index, y=time_prices.values, name='Average Price', marker_color='green'),
    row=1, col=2
)

# Duration vs days left
fig_time.add_trace(
    go.Scatter(x=df['days_left'], y=df['duration'], mode='markers',
               marker=dict(size=2, opacity=0.5, color=df['price'], colorscale='Viridis'),
               name='Duration vs Days'),
    row=2, col=1
)

# Time-based price trends
time_analysis = df.groupby('departure_time').agg({
    'price': ['mean', 'count'],
    'duration': 'mean'
}).reset_index()
time_analysis.columns = ['departure_time', 'avg_price', 'count', 'avg_duration']

fig_time.add_trace(
    go.Scatter(x=time_analysis['departure_time'], y=time_analysis['avg_price'],
               mode='lines+markers', name='Price Trend',
               line=dict(color='purple', width=3)),
    row=2, col=2
)

fig_time.update_layout(
    height=800,
    title_text="⏰ Time Analysis Dashboard",
    template='plotly_white',
    showlegend=True
)
fig_time.write_html('time_analysis_dashboard.html')

# 4. ROUTE AND AIRLINE ANALYSIS
print("🛫 Creating Route and Airline Analysis...")

fig_route = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Most Popular Routes',
        'Most Expensive Routes',
        'Airline Performance Comparison',
        'Route Price Heatmap'
    )
)

# Most popular routes
route_counts = df.groupby(['source_city', 'destination_city']).size().sort_values(ascending=False).head(10)
fig_route.add_trace(
    go.Bar(x=[f"{route[0]}→{route[1]}" for route in route_counts.index], 
           y=route_counts.values, name='Flight Count', marker_color='blue'),
    row=1, col=1
)

# Most expensive routes
route_prices = df.groupby(['source_city', 'destination_city'])['price'].mean().sort_values(ascending=False).head(10)
fig_route.add_trace(
    go.Bar(x=[f"{route[0]}→{route[1]}" for route in route_prices.index], 
           y=route_prices.values, name='Average Price', marker_color='red'),
    row=1, col=2
)

# Airline performance
airline_perf = df.groupby('airline').agg({
    'price': ['mean', 'count'],
    'duration': 'mean'
}).round(2)
airline_perf.columns = ['avg_price', 'flight_count', 'avg_duration']

fig_route.add_trace(
    go.Scatter(x=airline_perf['avg_duration'], y=airline_perf['avg_price'],
               mode='markers+text', text=airline_perf.index,
               marker=dict(size=airline_perf['flight_count']/1000, color='green'),
               name='Airline Performance'),
    row=2, col=1
)

# Route price heatmap
price_pivot = df.pivot_table(values='price', index='source_city', columns='destination_city', aggfunc='mean')
fig_route.add_trace(
    go.Heatmap(z=price_pivot.values, x=price_pivot.columns, y=price_pivot.index,
               colorscale='Viridis', name='Route Prices'),
    row=2, col=2
)

fig_route.update_layout(
    height=800,
    title_text="🛫 Route and Airline Analysis",
    template='plotly_white',
    showlegend=True
)
fig_route.write_html('route_airline_dashboard.html')

# 5. CREATE A BEAUTIFUL HTML DASHBOARD
print("🌐 Creating Beautiful HTML Dashboard...")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Airlines Data Analysis Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }
        .header {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .header h1 {
            margin: 0;
            color: #2c3e50;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .header p {
            margin: 10px 0 0 0;
            color: #7f8c8d;
            font-size: 1.1em;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        .stat-card:hover {
            transform: translateY(-5px);
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #3498db;
            margin-bottom: 10px;
        }
        .stat-label {
            color: #7f8c8d;
            font-size: 1.1em;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }
        .dashboard-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .dashboard-card:hover {
            transform: translateY(-5px);
        }
        .card-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 20px;
            font-size: 1.2em;
            font-weight: bold;
        }
        .card-content {
            padding: 20px;
        }
        .iframe-container {
            position: relative;
            width: 100%;
            height: 500px;
            overflow: hidden;
        }
        .iframe-container iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        .footer {
            text-align: center;
            padding: 30px;
            color: white;
            background: rgba(0,0,0,0.1);
            margin-top: 50px;
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        .nav-button {
            background: rgba(255, 255, 255, 0.95);
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            font-weight: bold;
            color: #2c3e50;
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .nav-button:hover {
            background: #3498db;
            color: white;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Airlines Data Analysis Dashboard</h1>
        <p>Comprehensive analysis of 300,153 flight records across Indian domestic airlines</p>
    </div>
    
    <div class="container">
        <div class="nav-buttons">
            <button class="nav-button" onclick="showSection('overview')">📊 Overview</button>
            <button class="nav-button" onclick="showSection('pricing')">💰 Pricing Analysis</button>
            <button class="nav-button" onclick="showSection('routes')">🛫 Routes & Airlines</button>
            <button class="nav-button" onclick="showSection('timing')">⏰ Time Analysis</button>
        </div>
        
        <div id="overview" class="section">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">300,153</div>
                    <div class="stat-label">Total Flights</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">6</div>
                    <div class="stat-label">Airlines</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">36</div>
                    <div class="stat-label">Routes</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">$20,890</div>
                    <div class="stat-label">Average Price</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">12.2h</div>
                    <div class="stat-label">Avg Duration</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">26</div>
                    <div class="stat-label">Avg Days Left</div>
                </div>
            </div>
            
            <div class="dashboard-grid">
                <div class="dashboard-card">
                    <div class="card-header">📊 Main Dashboard</div>
                    <div class="card-content">
                        <div class="iframe-container">
                            <iframe src="main_dashboard.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div id="pricing" class="section" style="display: none;">
            <div class="dashboard-grid">
                <div class="dashboard-card">
                    <div class="card-header">💰 Advanced Price Analysis</div>
                    <div class="card-content">
                        <div class="iframe-container">
                            <iframe src="advanced_price_dashboard.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div id="routes" class="section" style="display: none;">
            <div class="dashboard-grid">
                <div class="dashboard-card">
                    <div class="card-header">🛫 Route and Airline Analysis</div>
                    <div class="card-content">
                        <div class="iframe-container">
                            <iframe src="route_airline_dashboard.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div id="timing" class="section" style="display: none;">
            <div class="dashboard-grid">
                <div class="dashboard-card">
                    <div class="card-header">⏰ Time Analysis Dashboard</div>
                    <div class="card-content">
                        <div class="iframe-container">
                            <iframe src="time_analysis_dashboard.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>🎉 Interactive Airlines Data Analysis Dashboard | Created with Plotly & Python</p>
        <p>💡 Hover over charts for detailed information | Click and drag to zoom | Use legend to filter data</p>
    </div>
    
    <script>
        function showSection(sectionId) {
            // Hide all sections
            const sections = document.querySelectorAll('.section');
            sections.forEach(section => section.style.display = 'none');
            
            // Show selected section
            document.getElementById(sectionId).style.display = 'block';
            
            // Update button styles
            const buttons = document.querySelectorAll('.nav-button');
            buttons.forEach(button => button.style.background = 'rgba(255, 255, 255, 0.95)');
            buttons.forEach(button => button.style.color = '#2c3e50');
            
            // Highlight active button
            event.target.style.background = '#3498db';
            event.target.style.color = 'white';
        }
    </script>
</body>
</html>
"""

with open('beautiful_dashboard.html', 'w') as f:
    f.write(html_content)

print("\n" + "="*60)
print("🎉 BEAUTIFUL DASHBOARD CREATION COMPLETE!")
print("="*60)
print("\n📁 Generated Files:")
print("1. main_dashboard.html - Main comprehensive dashboard")
print("2. advanced_price_dashboard.html - Advanced price analysis")
print("3. time_analysis_dashboard.html - Time-based analysis")
print("4. route_airline_dashboard.html - Route and airline analysis")
print("5. beautiful_dashboard.html - Beautiful HTML dashboard with navigation")

print("\n🚀 Open 'beautiful_dashboard.html' in your browser for the complete experience!")
print("💡 Features:")
print("   - Interactive navigation between different analyses")
print("   - Responsive design with beautiful gradients")
print("   - Hover effects and smooth animations")
print("   - Embedded interactive Plotly charts")
print("   - Professional statistics cards")
print("   - Mobile-friendly layout") 