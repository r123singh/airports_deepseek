import folium
import pandas as pd

# Sample data
data = {
    "City": ["Atlanta", "Beijing", "Los Angeles", "Tokyo", "Dubai", "Chicago", "London", "Shanghai", "Paris", "Dallas", 
             "Guangzhou", "Amsterdam", "Frankfurt", "Istanbul", "Hong Kong", "Denver", "Singapore", "Seoul", "Bangkok", "New York"],
    "Airport": ["Hartsfield-Jackson Airport", "Beijing Capital International", "Los Angeles International", "Haneda Airport", 
                "Dubai International Airport", "O'Hare International Airport", "Heathrow Airport", "Pudong International Airport", 
                "Charles de Gaulle Airport", "Dallas/Fort Worth International", "Baiyun International Airport", "Schiphol Airport", 
                "Frankfurt Airport", "Istanbul Airport", "Hong Kong International Airport", "Denver International Airport", 
                "Changi Airport", "Incheon International Airport", "Suvarnabhumi Airport", "John F. Kennedy International"],
    "Latitude": [33.6407, 40.0801, 33.9416, 35.5494, 25.2532, 41.9742, 51.4700, 31.1434, 49.0097, 32.8998, 
                 23.3924, 52.3105, 50.0379, 41.2759, 22.3080, 39.8561, 1.3644, 37.4602, 13.6811, 40.6413],
    "Longitude": [-84.4277, 116.5845, -118.4085, 139.7798, 55.3657, -87.9073, -0.4543, 121.8052, 2.5479, -97.0403, 
                  113.2990, 4.7683, 8.5622, 28.7519, 113.9185, -104.6737, 103.9915, 126.4407, 100.7473, -73.7781],
    "Daily_Routes": [2700, 1700, 1500, 1400, 1300, 2300, 1800, 1600, 1400, 2000, 
                     1200, 1300, 1400, 1500, 1100, 1600, 1300, 1200, 1100, 1900],
    "Airline_Count": [50, 100, 70, 60, 90, 45, 80, 85, 75, 55, 
                      65, 60, 70, 80, 90, 50, 95, 85, 75, 65]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define thresholds for categories
high_threshold = 2000
moderate_threshold = 1500

# Function to assign color based on daily routes
def get_color(daily_routes):
    if daily_routes >= high_threshold:
        return 'red'  # High traffic
    elif daily_routes >= moderate_threshold:
        return 'orange'  # Moderate traffic
    else:
        return 'green'  # Low traffic

# Create a map centered at the first airport
map_center = [df.iloc[0]['Latitude'], df.iloc[0]['Longitude']]
m = folium.Map(location=map_center, zoom_start=2)

# Add markers for each airport
for index, row in df.iterrows():
    popup_text = f"City: {row['City']}<br>Airport: {row['Airport']}<br>Daily Routes: {row['Daily_Routes']}<br>Airlines: {row['Airline_Count']}"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_text,
        icon=folium.Icon(color=get_color(row['Daily_Routes']), icon='plane', prefix='fa')
    ).add_to(m)

# Save the map to an HTML file
m.save("busiest_airports_map.html")