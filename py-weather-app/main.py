import requests
import tkinter as tk
from tkinter import messagebox
from config import API_KEY, BASE_URL

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        result_label.config(text=f"Weather in {city}:\nTemperature: {temp}°C\nCondition: {description}")

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or API error.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

tk.Label(root, text="Enter city name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
