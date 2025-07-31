import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import altair as alt
from wordcloud import WordCloud
import folium
from folium import plugins
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set up the color palette for a modern look
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e', 
    'accent': '#2ca02c',
    'warning': '#d62728',
    'info': '#9467bd',
    'light': '#8c564b',
    'dark': '#e377c2',
    'success': '#17becf'
}

print("🚀 CREATING MODERN AIRLINES DASHBOARD")
print("="*60)

# Read the dataset
df = pd.read_csv('airlines_flights_data.csv')
print(f"📊 Dataset loaded: {df.shape[0]:,} flights, {df.shape[1]} features")

# 1. INTERACTIVE PRICE ANALYSIS DASHBOARD
print("\n💰 Creating Interactive Price Analysis...")

# Price distribution with interactive histogram
fig_price_dist = px.histogram(
    df, x='price', nbins=50,
    title='Interactive Price Distribution',
    labels={'price': 'Price ($)', 'count': 'Number of Flights'},
    color_discrete_sequence=[COLORS['primary']],
    opacity=0.8
)
fig_price_dist.add_vline(x=df['price'].median(), line_dash="dash", line_color=COLORS['warning'],
                        annotation_text=f"Median: ${df['price'].median():,.0f}")
fig_price_dist.update_layout(
    template='plotly_white',
    title_font_size=20,
    showlegend=False
)
fig_price_dist.write_html('price_distribution.html')

# Price by airline with interactive box plot
fig_airline_prices = px.box(
    df, x='airline', y='price', color='airline',
    title='Price Distribution by Airline',
    labels={'price': 'Price ($)', 'airline': 'Airline'},
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig_airline_prices.update_layout(
    template='plotly_white',
    title_font_size=20,
    xaxis_tickangle=-45
)
fig_airline_prices.write_html('airline_prices.html')

# 2. ADVANCED ROUTE ANALYSIS
print("🛫 Creating Advanced Route Analysis...")

# Route popularity heatmap
route_matrix = df.groupby(['source_city', 'destination_city']).size().unstack(fill_value=0)
fig_route_heatmap = px.imshow(
    route_matrix, 
    title='Route Popularity Heatmap',
    labels=dict(x="Destination City", y="Source City", color="Number of Flights"),
    color_continuous_scale='Viridis',
    aspect="auto"
)
fig_route_heatmap.update_layout(
    template='plotly_white',
    title_font_size=20
)
fig_route_heatmap.write_html('route_heatmap.html')

# 3. INTERACTIVE TIME SERIES ANALYSIS
print("⏰ Creating Time Series Analysis...")

# Price trends by departure time
time_price_analysis = df.groupby('departure_time')['price'].agg(['mean', 'count']).reset_index()
fig_time_price = px.bar(
    time_price_analysis, x='departure_time', y='mean',
    title='Average Price by Departure Time',
    labels={'mean': 'Average Price ($)', 'departure_time': 'Departure Time'},
    color='count',
    color_continuous_scale='Plasma',
    text=time_price_analysis['mean'].round(0)
)
fig_time_price.update_traces(texttemplate='$%{text:,}', textposition='outside')
fig_time_price.update_layout(
    template='plotly_white',
    title_font_size=20,
    xaxis_tickangle=-45
)
fig_time_price.write_html('time_price_analysis.html')

# 4. 3D SCATTER PLOT - PRICE VS DURATION VS DAYS LEFT
print("🎯 Creating 3D Scatter Plot...")

fig_3d = px.scatter_3d(
    df.sample(5000), x='price', y='duration', z='days_left',
    color='airline', size='price',
    title='3D Analysis: Price vs Duration vs Days Left',
    labels={'price': 'Price ($)', 'duration': 'Duration (hours)', 'days_left': 'Days Left'},
    opacity=0.7
)
fig_3d.update_layout(
    template='plotly_white',
    title_font_size=20,
    scene=dict(
        xaxis_title="Price ($)",
        yaxis_title="Duration (hours)",
        zaxis_title="Days Left"
    )
)
fig_3d.write_html('3d_analysis.html')

# 5. INTERACTIVE MAP VISUALIZATION
print("🗺️ Creating Interactive Map...")

# Create a map centered on India
m = folium.Map(
    location=[20.5937, 78.9629],  # Center of India
    zoom_start=5,
    tiles='CartoDB positron'
)

# Add city markers with flight information
cities = {
    'Delhi': [28.7041, 77.1025],
    'Mumbai': [19.0760, 72.8777],
    'Bangalore': [12.9716, 77.5946],
    'Kolkata': [22.5726, 88.3639],
    'Hyderabad': [17.3850, 78.4867],
    'Chennai': [13.0827, 80.2707]
}

for city, coords in cities.items():
    city_flights = df[df['source_city'] == city].shape[0]
    avg_price = df[df['source_city'] == city]['price'].mean()
    
    folium.Marker(
        coords,
        popup=f"""
        <b>{city}</b><br>
        Total Flights: {city_flights:,}<br>
        Avg Price: ${avg_price:,.0f}
        """,
        tooltip=city,
        icon=folium.Icon(color='red', icon='plane')
    ).add_to(m)

m.save('interactive_map.html')

# 6. ADVANCED STATISTICAL VISUALIZATIONS
print("📊 Creating Advanced Statistical Visualizations...")

# Correlation heatmap
numeric_cols = ['price', 'duration', 'days_left']
correlation_matrix = df[numeric_cols].corr()

fig_corr = px.imshow(
    correlation_matrix,
    title='Feature Correlation Heatmap',
    color_continuous_scale='RdBu',
    aspect="auto"
)
fig_corr.update_layout(
    template='plotly_white',
    title_font_size=20
)
fig_corr.write_html('correlation_heatmap.html')

# 7. WORD CLOUD FOR AIRLINES
print("☁️ Creating Word Cloud...")

# Create word cloud based on airline frequency
airline_freq = df['airline'].value_counts()
wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='viridis',
    max_words=100
).generate_from_frequencies(airline_freq)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Airline Frequency Word Cloud', fontsize=20, pad=20)
plt.tight_layout()
plt.savefig('airline_wordcloud.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. INTERACTIVE DASHBOARD WITH SUBPLOTS
print("📈 Creating Interactive Dashboard...")

# Create a comprehensive dashboard
fig_dashboard = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Price Distribution by Class',
        'Duration vs Price Scatter',
        'Market Share by Airline',
        'Booking Patterns by Days Left',
        'Price Range by Route',
        'Stop Analysis'
    ),
    specs=[
        [{"type": "bar"}, {"type": "scatter"}],
        [{"type": "pie"}, {"type": "bar"}],
        [{"type": "box"}, {"type": "violin"}]
    ]
)

# 1. Price by class
class_prices = df.groupby('class')['price'].mean()
fig_dashboard.add_trace(
    go.Bar(x=class_prices.index, y=class_prices.values, name='Class Prices', marker_color=COLORS['primary']),
    row=1, col=1
)

# 2. Duration vs Price scatter
sample_df = df.sample(1000)
fig_dashboard.add_trace(
    go.Scatter(x=sample_df['duration'], y=sample_df['price'], mode='markers', 
               name='Duration vs Price', marker=dict(color=COLORS['secondary'], opacity=0.6)),
    row=1, col=2
)

# 3. Market share pie chart
market_share = df['airline'].value_counts()
fig_dashboard.add_trace(
    go.Pie(labels=market_share.index, values=market_share.values, name='Market Share'),
    row=2, col=1
)

# 4. Booking patterns
days_bins = pd.cut(df['days_left'], bins=[0, 7, 14, 30, 49], labels=['1-7', '8-14', '15-30', '31-49'])
booking_patterns = df.groupby(days_bins)['price'].mean()
fig_dashboard.add_trace(
    go.Bar(x=booking_patterns.index.astype(str), y=booking_patterns.values, name='Booking Patterns', marker_color=COLORS['accent']),
    row=2, col=2
)

# 5. Price by route (top 10)
route_prices = df.groupby(['source_city', 'destination_city'])['price'].mean().sort_values(ascending=False).head(10)
fig_dashboard.add_trace(
    go.Box(x=df['source_city'], y=df['price'], name='Route Prices', marker_color=COLORS['info']),
    row=3, col=1
)

# 6. Stop analysis
fig_dashboard.add_trace(
    go.Violin(x=df['stops'], y=df['price'], name='Stop Analysis', marker_color=COLORS['light']),
    row=3, col=2
)

fig_dashboard.update_layout(
    height=1200,
    title_text="Comprehensive Airlines Dashboard",
    template='plotly_white',
    showlegend=False
)

fig_dashboard.write_html('comprehensive_dashboard.html')

# 9. ANIMATED VISUALIZATIONS
print("🎬 Creating Animated Visualizations...")

# Animated price trends by airline over days left
df_animated = df.groupby(['airline', 'days_left'])['price'].mean().reset_index()
fig_animated = px.scatter(
    df_animated, x='days_left', y='price', color='airline', size='price',
    title='Animated Price Trends by Airline',
    labels={'price': 'Average Price ($)', 'days_left': 'Days Before Departure'},
    animation_frame='days_left',
    range_x=[1, 49], range_y=[0, 50000]
)
fig_animated.update_layout(
    template='plotly_white',
    title_font_size=20
)
fig_animated.write_html('animated_price_trends.html')

# 10. ADVANCED ALTAR CHART
print("📊 Creating Altair Chart...")

# Create an interactive Altair chart
alt.data_transformers.enable('default', max_rows=None)

# Price distribution by airline and class
chart = alt.Chart(df.sample(10000)).mark_circle().encode(
    x=alt.X('price:Q', title='Price ($)'),
    y=alt.Y('duration:Q', title='Duration (hours)'),
    color=alt.Color('airline:N', title='Airline'),
    size=alt.Size('days_left:Q', title='Days Left'),
    tooltip=['airline', 'price', 'duration', 'days_left', 'class']
).properties(
    title='Interactive Price-Duration Analysis',
    width=800,
    height=400
).interactive()

chart.save('altair_chart.html')

# 11. STATISTICAL SUMMARY DASHBOARD
print("📋 Creating Statistical Summary...")

# Create a beautiful statistical summary
stats_summary = {
    'Total Flights': f"{df.shape[0]:,}",
    'Total Airlines': f"{df['airline'].nunique()}",
    'Total Routes': f"{df.groupby(['source_city', 'destination_city']).ngroups}",
    'Average Price': f"${df['price'].mean():,.0f}",
    'Median Price': f"${df['price'].median():,.0f}",
    'Price Range': f"${df['price'].min():,.0f} - ${df['price'].max():,.0f}",
    'Average Duration': f"{df['duration'].mean():.1f} hours",
    'Most Popular Route': f"{df.groupby(['source_city', 'destination_city']).size().idxmax()[0]} → {df.groupby(['source_city', 'destination_city']).size().idxmax()[1]}",
    'Market Leader': f"{df['airline'].value_counts().index[0]} ({df['airline'].value_counts().iloc[0]/len(df)*100:.1f}%)"
}

# Create a beautiful summary table
fig_summary = go.Figure(data=[go.Table(
    header=dict(
        values=['Metric', 'Value'],
        fill_color=COLORS['primary'],
        font=dict(color='white', size=14),
        align='left'
    ),
    cells=dict(
        values=[list(stats_summary.keys()), list(stats_summary.values())],
        fill_color='lavender',
        font=dict(size=12),
        align='left'
    )
)])

fig_summary.update_layout(
    title='Dataset Summary Statistics',
    template='plotly_white',
    title_font_size=20
)
fig_summary.write_html('summary_statistics.html')

print("\n" + "="*60)
print("🎉 MODERN DASHBOARD CREATION COMPLETE!")
print("="*60)
print("\n📁 Generated Files:")
print("1. price_distribution.html - Interactive price histogram")
print("2. airline_prices.html - Box plots by airline")
print("3. route_heatmap.html - Route popularity heatmap")
print("4. time_price_analysis.html - Price by departure time")
print("5. 3d_analysis.html - 3D scatter plot")
print("6. interactive_map.html - Interactive map of India")
print("7. correlation_heatmap.html - Feature correlations")
print("8. airline_wordcloud.png - Airline frequency word cloud")
print("9. comprehensive_dashboard.html - Multi-panel dashboard")
print("10. animated_price_trends.html - Animated price trends")
print("11. altair_chart.html - Interactive Altair visualization")
print("12. summary_statistics.html - Statistical summary table")

print("\n🚀 Open any .html file in your browser to view the interactive visualizations!")
print("💡 All visualizations are interactive and can be zoomed, panned, and explored!") 