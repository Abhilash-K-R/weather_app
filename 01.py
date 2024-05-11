
import tkinter as tk
from tkinter import ttk
import requests


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=20)

        # Weather information labels
        ttk.Label(self.main_frame, text="Current Weather", font=("Helvetica", 16, "bold")).grid(row=0, column=0,
                                                                                                columnspan=2, pady=10)
        ttk.Label(self.main_frame, text="Location:").grid(row=1, column=0, sticky="E", padx=5)
        self.location_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.location_label.grid(row=1, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Temperature:").grid(row=2, column=0, sticky="E", padx=5)
        self.temp_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.temp_label.grid(row=2, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Humidity:").grid(row=3, column=0, sticky="E", padx=5)
        self.humidity_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.humidity_label.grid(row=3, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Wind Speed:").grid(row=4, column=0, sticky="E", padx=5)
        self.wind_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.wind_label.grid(row=4, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Visibility:").grid(row=5, column=0, sticky="E", padx=5)
        self.visibility_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.visibility_label.grid(row=5, column=1, sticky="W", padx=5)

        # Update weather information button
        self.update_button = ttk.Button(self.main_frame, text="Update", command=self.update_weather)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Initial weather data
        self.update_weather()

    def update_weather(self):
        try:
            # Call OpenWeatherMap API to fetch weather data
            api_key = "YOUR_OPENWEATHERMAP_API_KEY"
            city = "New York"  # Default city
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

            # Fetch weather data
            response = requests.get(url)
            weather_data = response.json()

            # Print full response data for inspection
            print(weather_data)

            # Extract relevant weather information
            location = weather_data["name"]
            temperature = f"{weather_data['main']['temp']}°C"
            humidity = f"{weather_data['main']['humidity']}%"
            wind_speed = f"{weather_data['wind']['speed']} m/s"
            visibility = f"{weather_data['visibility']} meters"

            # Update labels with weather information
            self.location_label.config(text=location)
            self.temp_label.config(text=temperature)
            self.humidity_label.config(text=humidity)
            self.wind_label.config(text=wind_speed)
            self.visibility_label.config(text=visibility)

        except Exception as e:
            # Handle any errors that occur during API request or data parsing
            print("Error fetching weather data:", e)


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()

