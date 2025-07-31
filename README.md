# 🚀 Airlines Data Analysis Dashboard

A comprehensive, interactive dashboard for analyzing Indian domestic airlines flight data with state-of-the-art visualizations and advanced analytics.

![Dashboard Preview](https://img.shields.io/badge/Dashboard-Interactive-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)
![Data Science](https://img.shields.io/badge/Data-Science-purple)

## 📊 Project Overview

This project analyzes **300,153 flight records** from Indian domestic airlines, providing deep insights into pricing patterns, route optimization, market dynamics, and booking behaviors. The analysis includes interactive visualizations, statistical modeling, and business intelligence insights.

### 🎯 Key Features

- **Interactive Dashboard** with modern UI/UX design
- **18+ Advanced Visualizations** using Plotly, Altair, and other libraries
- **Real-time Data Analysis** with comprehensive statistics
- **Business Intelligence Insights** for strategic decision-making
- **Responsive Design** that works on all devices
- **Professional-grade Analytics** suitable for presentations

## 📈 Dataset Information

### Dataset: `airlines_flights_data.csv`
- **Size**: 300,153 records, 12 features
- **Memory**: 27.5+ MB
- **Quality**: No missing values, complete dataset

### Features Analyzed:
1. **index** - Record identifier
2. **airline** - Airline name (6 airlines: Vistara, Air India, Indigo, GO_FIRST, AirAsia, SpiceJet)
3. **flight** - Flight number
4. **source_city** - Departure city (6 cities: Delhi, Mumbai, Bangalore, Kolkata, Hyderabad, Chennai)
5. **departure_time** - Time of departure (6 categories)
6. **stops** - Number of stops (zero, one, two_or_more)
7. **arrival_time** - Time of arrival (6 categories)
8. **destination_city** - Arrival city
9. **class** - Travel class (Economy/Business)
10. **duration** - Flight duration in hours
11. **days_left** - Days until departure (1-49 days)
12. **price** - Ticket price in dollars

## 🎨 Visualizations Created

### 📊 Main Dashboard Files:
1. **`beautiful_dashboard.html`** ⭐ - **Main interactive dashboard with navigation**
2. **`main_dashboard.html`** - Comprehensive 6-panel dashboard
3. **`advanced_price_dashboard.html`** - Sophisticated price analysis
4. **`time_analysis_dashboard.html`** - Time-based trends
5. **`route_airline_dashboard.html`** - Route and airline analysis

### 📈 Individual Interactive Visualizations:
6. **`price_distribution.html`** - Interactive price histogram
7. **`airline_prices.html`** - Box plots by airline
8. **`route_heatmap.html`** - Route popularity heatmap
9. **`3d_analysis.html`** - 3D scatter plot
10. **`interactive_map.html`** - Interactive map of India
11. **`correlation_heatmap.html`** - Feature correlations
12. **`comprehensive_dashboard.html`** - Multi-panel dashboard
13. **`animated_price_trends.html`** - Animated price trends
14. **`altair_chart.html`** - Interactive Altair visualization
15. **`summary_statistics.html`** - Statistical summary table
16. **`time_price_analysis.html`** - Price by departure time
17. **`time_series_analysis.html`** - Advanced time series

### 🖼️ Static Visualizations:
18. **`airline_wordcloud.png`** - Airline frequency word cloud
19. **`price_analysis.png`** - Price analysis charts

## 🔍 Key Insights Discovered

### 💰 Pricing Analysis:
- **Price Range**: $1,105 - $123,071
- **Average Price**: $20,890
- **Median Price**: $7,425
- **Most Expensive Airline**: Vistara ($30,397 avg)
- **Most Affordable Airline**: AirAsia ($4,091 avg)
- **Business Class Premium**: Significantly higher than Economy

### 🛫 Route Analysis:
- **Busiest Route**: Delhi → Mumbai (15,289 flights)
- **Most Expensive Route**: Chennai → Bangalore ($25,082 avg)
- **Total Routes**: 36 unique city pairs
- **Route Popularity**: Major metro cities dominate

### ⏰ Time Patterns:
- **Peak Departure Time**: Morning (23.7% of flights)
- **Most Expensive Time**: Night flights ($23,062 avg)
- **Best Value Time**: Early morning ($20,371 avg)
- **Booking Patterns**: Prices increase as departure approaches

### 📊 Market Analysis:
- **Market Leader**: Vistara (42.6% market share)
- **Total Airlines**: 6 major carriers
- **Flight Distribution**: Economy dominates (69% vs 31% Business)
- **Stop Patterns**: 83.6% have one stop

## 🚀 Getting Started

### Prerequisites:
```bash
Python 3.8+
pip install -r requirements.txt
```

### Installation:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Flight_data_log.git
   cd Flight_data_log
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis**:
   ```bash
   python modern_dashboard.py
   python beautiful_dashboard.py
   ```

4. **Open the dashboard**:
   ```bash
   open beautiful_dashboard.html
   ```

## 📁 Project Structure

```
Flight_data_log/
├── airlines_flights_data.csv          # Main dataset
├── requirements.txt                   # Python dependencies
├── read_dataset.py                   # Basic data reading script
├── data_analysis_explorer.py         # Comprehensive analysis
├── modern_dashboard.py               # Modern visualizations
├── beautiful_dashboard.py            # Beautiful dashboard creation
├── beautiful_dashboard.html          # ⭐ Main interactive dashboard
├── main_dashboard.html               # Comprehensive dashboard
├── advanced_price_dashboard.html     # Price analysis
├── time_analysis_dashboard.html      # Time-based analysis
├── route_airline_dashboard.html      # Route analysis
├── [18 other visualization files]    # Individual charts
└── README.md                         # This file
```

## 🛠️ Technologies Used

### Core Libraries:
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualizations
- **Altair** - Declarative visualization
- **Matplotlib** - Static plotting
- **Seaborn** - Statistical visualization
- **Folium** - Interactive maps
- **WordCloud** - Text visualization

### Advanced Analytics:
- **SciPy** - Statistical analysis
- **Scikit-learn** - Machine learning (for future enhancements)

## 🎯 Use Cases

### For Airlines:
- **Revenue optimization** and pricing strategies
- **Route planning** and expansion decisions
- **Competitive analysis** and market positioning
- **Customer behavior** insights
- **Operational efficiency** improvements

### For Travel Platforms:
- **Price comparison** engines
- **Recommendation systems** development
- **Demand forecasting** models
- **Dynamic pricing** algorithms
- **Customer segmentation** analysis

### For Customers:
- **Best time to book** analysis
- **Price tracking** and alerts
- **Route optimization** tools
- **Airline comparison** platforms

## 📊 Analytics Capabilities

### Statistical Analysis:
- **Descriptive statistics** for all variables
- **Correlation analysis** between features
- **Distribution fitting** and normality tests
- **Outlier detection** and analysis
- **Trend analysis** and forecasting

### Business Intelligence:
- **Market share analysis** by airline
- **Revenue potential** calculations
- **Price elasticity** analysis
- **Route profitability** assessment
- **Seasonal pattern** identification

### Predictive Modeling Ready:
- **Price prediction** models
- **Demand forecasting** capabilities
- **Customer churn** prediction
- **Route recommendation** systems
- **Revenue optimization** algorithms

## 🎨 Dashboard Features

### Interactive Elements:
- **Hover tooltips** with detailed information
- **Click and drag** zoom functionality
- **Legend filtering** for data exploration
- **Responsive design** for all screen sizes
- **Smooth animations** and transitions

### Navigation:
- **Tab-based navigation** between analyses
- **Breadcrumb navigation** for easy orientation
- **Search functionality** for specific insights
- **Export capabilities** for reports

### Visual Design:
- **Modern gradient backgrounds**
- **Professional color schemes**
- **Typography optimization**
- **Mobile-responsive layout**
- **Accessibility features**

## 🔮 Future Enhancements

### Planned Features:
- **Real-time data integration**
- **Machine learning models** for price prediction
- **API endpoints** for data access
- **User authentication** and personalization
- **Advanced filtering** and search
- **Export to PDF/Excel** functionality
- **Email alerts** for price changes
- **Mobile app** development

### Technical Improvements:
- **Database integration** for larger datasets
- **Cloud deployment** for scalability
- **Performance optimization** for real-time updates
- **Advanced caching** mechanisms
- **API documentation** and testing

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests if applicable**
5. **Submit a pull request**

### Development Setup:
```bash
git clone https://github.com/yourusername/Flight_data_log.git
cd Flight_data_log
pip install -r requirements.txt
python -m pytest  # Run tests
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset Source**: Indian domestic airlines flight data
- **Visualization Libraries**: Plotly, Altair, Matplotlib, Seaborn
- **Analysis Tools**: Pandas, NumPy, SciPy
- **Design Inspiration**: Modern dashboard design principles

## 📞 Contact

- **Project Link**: [https://github.com/yourusername/Flight_data_log](https://github.com/yourusername/Flight_data_log)
- **Issues**: [GitHub Issues](https://github.com/yourusername/Flight_data_log/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/Flight_data_log/discussions)

---

⭐ **Star this repository if you find it helpful!**

🚀 **Ready to explore your airlines data? Open `beautiful_dashboard.html` in your browser!**